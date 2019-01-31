#data
dataroot='../../datasets/ICDAR_2015_IndidentalSceneText/train/'  #./data/train/img      ./data/train/gt
test_img_path='../../datasets/ICDAR_2015_IndidentalSceneText/test/img'
result = '../../datasets/ICDAR_2015_IndidentalSceneText/results'

training_data_path = '../../datasets/ICDAR_2015_IndidentalSceneText/training/loss.txt'

lr = 0.0001
gpu_ids = [0]
gpu = 1
init_type = 'xavier'

resume = False
checkpoint = ''# should be file
train_batch_size_per_gpu  = 16
num_workers = 1

print_freq = 1
eval_iteration = 50
save_iteration = 50
max_epochs = 1000000







