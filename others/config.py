import configparser

config = configparser.ConfigParser()
config['hyperparameters'] = {
    'batch_sizes' : [16, 128],
    'num_epochs' : 20,
    'learning_rate' : 0.01,
    'embed_dims' : 512,
    'num_lstm_units' : 512,
    'num_lstm_layers' : 2,
    'num_output_classes' : 1
}

path = r"D:\\Data\\Documents\\Rafi\\Python Scripts\\Spam_Classifier_LSTM_PyTorch\\"
filename = "config.ini"
with open(path + filename, 'w') as conf:
    config.write(conf)
