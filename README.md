# FCN-tensorflow
Tensorflow implementation of Fully Convolutional Networks for Semantic Segmentation (FCNs).

The implementation is largely based on the reference code provided by the authors of the paper link. The model was applied on the Scene Parsing Challenge dataset provided by MIT http://sceneparsing.csail.mit.edu/.

Note:I copy the codes from https://github.com/shekkizh/FCN.tensorflow/ and exchange some code in order to apply to my computer.

# My envirnment 
GPU:Titan xp

cuda:8+9

cudnn:7.05 for cuda 9

tensorflow1.4

python3.5

windows10

# Detail
1.I set lr=1e-5 batch_size=16 train the dataset=ADEChallengeData2016 (URL=http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip) model=VGG19(http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat)

I didn't  implement getdatafunction I directly download them form URL

2.I run the project in spyder

3.the training cost me about 20 hours(step max),loss is about 0.5 but val loss is about 2,I believe it can be improved.
I also train the model at lr=1e-4 batch_size=2, the result is so poor,output is always darkness

# Observations
loss
![image](https://github.com/ygjwd12345/FCN-tensorflow-win10/blob/master/logs/result1.png)

result
![image](https://github.com/ygjwd12345/FCN-tensorflow-win10/blob/master/logs/result2.png)
