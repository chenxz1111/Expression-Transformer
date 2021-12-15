import argparse
from numpy import arange, random
from torch import save, load, no_grad, LongTensor
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from data_generator import DataGenerator
from model import TransformerModel
from expression_loader import ExpressionLoader

def train(model, criterion, optimizer, loader):
    model.train()
    epoch_loss = 0
    for i, batch in enumerate(loader):
        src, tgt = batch
        src, tgt = src.transpose(1, 0).cuda(), tgt.transpose(1, 0).cuda()
        optimizer.zero_grad()
        output = model(src, tgt[:-1, :])
        n = output.shape[-1]
        loss = criterion(output.reshape(-1, n), tgt[1:, :].reshape(-1))
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        epoch_loss += loss.item()
    return epoch_loss / len(loader)


def validation(model, criterion, loader):
    model.eval()
    epoch_loss = 0
    with no_grad():
        for i, batch in enumerate(loader):
            src, tgt = batch
            src, tgt = src.transpose(1, 0).cuda(), tgt.transpose(1, 0).cuda()
            output = model(src, tgt[:-1, :])
            n = output.shape[-1]
            loss = criterion(output.reshape(-1, n), tgt[1:, :].reshape(-1))
            epoch_loss += loss.item()
    return epoch_loss / len(loader)


def test(model, test_expr, test_res):
    model = model.cuda()
    model.eval()
    with no_grad():
        cnt = 0
        for i in range(len(test_expr)):
            cpu_src = test_expr[i]
            src = LongTensor(cpu_src).unsqueeze(1).cuda()
            tgt = [0] + test_res[i]
            pred = [0]
            for j in range(len(test_res[i])):
                inp = LongTensor(pred).unsqueeze(1).cuda()
                output = model(src, inp)
                out_num = output.argmax(2)[-1].item()
                pred.append(out_num)
#             print("input: ", cpu_src)
#             print("target: ", tgt)
#             print("predict: ", pred)
            if tgt[1] == pred[1]: cnt += 1
        print (cnt)


def main(model_name=None, hidden=128, nlayers=4, batch_size=400, epoch=200):
    print ('num_layers:', nlayers, '\nbatchsize:', batch_size, '\nepoch:', epoch)
    epochs = 200
    
    in_voc_size, expr_list, res_list = ExpressionLoader('train')
    out_voc_size = 3
    print('in_voc_size: ', in_voc_size)
    dataset = DataGenerator(expr_list, res_list)
    train_len = int(len(dataset) * 0.9)
    val_len = len(dataset) - train_len
    train_set, val_set = random_split(dataset, [train_len, val_len])
    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=1)
    val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=True, num_workers=1)
    model = TransformerModel(in_voc_size, out_voc_size, hidden=hidden, nlayers=nlayers)
    if model_name is not None:
        model.load_state_dict(load(model_name))
    model = model.cuda()
    optimizer = optim.Adam(model.parameters())

    criterion = nn.CrossEntropyLoss(ignore_index=0)
    best_loss = 100
    for i in range(epochs):
        epoch_loss = train(model, criterion, optimizer, train_loader)
        epoch_loss_val = validation(model, criterion, val_loader)
    
        print("epoch: {} train loss: {}".format(i, epoch_loss))
        print("epoch: {} val loss: {}".format(i, epoch_loss_val))
        if epoch_loss_val < best_loss or 1:
            best_loss = epoch_loss_val
            model_name = "model/model_{0:.5f}.pt".format(epoch_loss_val)
            save(model.state_dict(), model_name)
    return model_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A PyTorch Transformer Language Model for Predicting Expression Value')
    parser.add_argument('--test_model', type=str, help='the model file to load')
    parser.add_argument('--train_model', type=str, help='the model file to load')
    parser.add_argument('--batch_size', type=int, default=400)
    parser.add_argument('--num_layers', type=int, default=4)
    parser.add_argument('--epoch', type=int, default=200)
    args = parser.parse_args()
    hidden = 128
    nlayers = args.num_layers
    batch_size = args.batch_size
    epoch = args.epoch
    if args.test_model is None:
        if args.train_model is not None:
            model_name = main(args.train_model, hidden=hidden, nlayers=nlayers, batch_size=batch_size, epoch=epoch)
        else:
            model_name = main(hidden=hidden, nlayers=nlayers, batch_size=batch_size, epoch=epoch)
    else:
        model_name = args.test_model
#         in_voc_size, expr_list, res_list = ExpressionLoader('train')
        in_voc_size, expr_list, res_list = ExpressionLoader('test')
        out_voc_size = 3
        model = TransformerModel(in_voc_size, out_voc_size, hidden=hidden, nlayers=nlayers)
        model.load_state_dict(load(model_name))
        test(model, test_expr=expr_list, test_res=res_list)
