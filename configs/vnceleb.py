from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.loss = "arcface"
config.network = "mbf"
config.resume = False
config.savedCheckpoint = "checkpoint_vn.pt"
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

config.rec = "./../../../VN_Celeb_train"
config.num_classes = 1020
config.num_image = 23105
config.num_epoch = 40
config.warmup_epoch = 0
config.val_targets = ['lfw']
