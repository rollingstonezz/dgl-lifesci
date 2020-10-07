# -*- coding: utf-8 -*-
#
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#
# pylint: disable= no-member, arguments-differ, invalid-name
#
# Pre-trained models on BACE

import torch.nn.functional as F

from ...model_zoo import *

__all__ = ['bace_url',
           'create_bace_model']

bace_url = {
    'GCN_canonical_BACE': 'dgllife/pre_trained/gcn_canonical_bace.pth',
    'GCN_attentivefp_BACE': 'dgllife/pre_trained/gcn_attentivefp_bace.pth'
}

def create_bace_model(model_name):
    """Create a model.

    Parameters
    ----------
    model_name : str
        Name for the model.

    Returns
    -------
    Created model
    """
    n_tasks = 1

    if model_name == 'GCN_canonical_BACE':
        dropout = 0.022033656211803594
        return GCNPredictor(in_feats=74,
                            hidden_feats=[128],
                            activation=[F.relu],
                            residual=[True],
                            batchnorm=[False],
                            dropout=[dropout],
                            predictor_hidden_feats=16,
                            predictor_dropout=dropout,
                            n_tasks=n_tasks)

    elif model_name == 'GCN_attentivefp_BACE':
        dropout = 0.009923177126280991
        num_gnn_layers = 2
        return GCNPredictor(in_feats=39,
                            hidden_feats=[64] * num_gnn_layers,
                            activation=[F.relu] * num_gnn_layers,
                            residual=[False] * num_gnn_layers,
                            batchnorm=[False] * num_gnn_layers,
                            dropout=[dropout] * num_gnn_layers,
                            predictor_hidden_feats=256,
                            predictor_dropout=dropout,
                            n_tasks=n_tasks)

    else:
        return None
