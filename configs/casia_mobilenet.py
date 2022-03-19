from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.loss = "arcface"
config.network = "mbf"
config.resume = True
config.savedCheckpoint = "checkpoint.pt"
config.output = None
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 1e-4
config.batch_size = 128
config.lr = 0.2
config.verbose = 2000
config.dali = False

config.rec = "./../../../faces_webface_112x112"
config.num_classes = 10572
config.num_image = 490623
config.num_epoch = 5
config.warmup_epoch = 0
config.val_targets = ['lfw']
