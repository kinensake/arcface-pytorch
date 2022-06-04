from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.loss = "arcface"
config.network = "mb3"
config.resume = False
config.savedCheckpoint = "checkpoint.pt"
config.output = None
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 1e-4
config.batch_size = 256
config.lr = 0.2
config.verbose = 5000
config.dali = False

config.rec = "./../../../faces_emore"
config.num_classes = 85742
config.num_image = 5800000
config.num_epoch = 40
config.warmup_epoch = 2
config.val_targets = ['lfw']
