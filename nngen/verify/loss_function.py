from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np

def cross_entropy_loss(ctx, weight, target, reduction='mean'):
    softmax = np.exp(weight)
    softmax /= softmax.sum(axis=1, keepdims=True)
    softmax = np.clip(softmax, 1e-10, None)
    ctx.save_for_backward(softmax, target)

    loss = -(np.log(softmax) * target).sum(axis=1)
    if reduction == 'mean':
        return loss.sum() / loss.size
    elif reduction == 'sum':
        return loss.sum()
    elif reduction == "none":
        return loss
    else:
        raise ValueError("reduction must be 'mean', 'sum' or 'none'")
