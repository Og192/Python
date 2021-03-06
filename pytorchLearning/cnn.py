#!/usr/bin/python3
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional

input = Variable(torch.ones(1, 1, 3, 5))
# inputFeatureMapSize, outputFeatureMapSize, kernelSize
m = nn.Conv1d(1, 1, (1, 3), stride=(1, 1), padding=(0, 1), bias=False)
# batchSize, featureMapSize, elementShape
print(input)
for para in m.parameters():
    print(para)
    print(torch.sum(para))
output = m(input)
print(output)


print("=================2d conv================")
m = nn.Conv2d(1, 10, (1, 3), stride=2, padding=(0, 0), bias=False)
pooling = nn.MaxPool2d((1, 2), stride=1)

input = Variable(torch.ones(1, 1, 3, 5))
print(input)
for para in m.parameters():
    print(para)
    print(torch.sum(para))
output = m(input)
print(output)

poolingResult = pooling(output)
print(poolingResult)
print("max for myself")
print(output.view(1, 10, -1))
poolingResult = torch.max(output.view(1, 10, -1), 2)
print(poolingResult[0])
print(poolingResult[0].size())

print("====================Pooling=====================")
v1 = Variable(torch.randn(1, 3, 4))
v2 = Variable(torch.randn(1, 3, 4))
v3 = Variable(torch.randn(1, 3, 4))

v = torch.cat([v1, v2, v3])
print(v)
print(torch.max(v, 0)[0].view(3, 4))

    # 2d
    # f = ConvNd(_single(stride), _single(padding), _single(dilation), False,
    #            _single(0), groups, torch.backends.cudnn.benchmark, torch.backends.cudnn.enabled)
    # return f(input, weight, bias)

    # 1d
    # f = ConvNd(_pair(stride), _pair(padding), _pair(dilation), False,
    #            _pair(0), groups, torch.backends.cudnn.benchmark, torch.backends.cudnn.enabled)
    # return f(input, weight, bias)

    # 3d
    # f = ConvNd(_triple(stride), _triple(padding), _triple(dilation), False,
    #            _triple(0), groups, torch.backends.cudnn.benchmark, torch.backends.cudnn.enabled)
    # return f(input, weight, bias)