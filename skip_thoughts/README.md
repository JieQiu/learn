#安装bazel https://docs.bazel.build/versions/master/install-ubuntu.html
```shell
Step 1: Download Bazel
proxychains wget https://github.com/bazelbuild/bazel/releases/download/0.12.0/bazel-0.12.0-installer-linux-x86_64.sh
Step 2: Run the installer
chmod +x bazel-<version>-installer-linux-x86_64.sh
./bazel-<version>-installer-linux-x86_64.sh --user
##The --user flag installs Bazel to the $HOME/bin directory on your system and sets the .bazelrc path to $HOME/.bazelrc. Use the --help command to see additional installation options.##
#source /home/qiujie/.bazel/bin/bazel-complete.bash 这句话加到～/.bashrc可以试试#
Step 3: Set up your environment<br>
##If you ran the Bazel installer with the --user flag as above, the Bazel executable is installed in your $HOME/bin directory. It's a good idea to add this directory to your default paths, as follows:##
export PATH="$PATH:$HOME/bin"##必须有才可以##
Step 4:
source ~/.bashrc
```
bazel：https://blog.csdn.net/elaine_bao/article/details/78668657
几点理解：BUILD是把文件依赖关系写清楚
bazel build -c编译。bazel-bin/运行(在进入有bazel-bin的文件下，执行地址也是平行相对的地址)。

开始：引用https://github.com/tensorflow/models/tree/master/research/skip_thoughts
### 1Prepare the Training Data
路径/home/qiujie/model/skipthoughts/...
数据/home/qiujie/model/skipthoughts/bookcorpus-->/home/qiujie/model/skipthoughts/data
/home/qiujie/model/bazel-bin
```shell
#each sentence is already tokenized.
INPUT_FILES="${HOME}/model/skip_thoughts/bookcorpus/*.txt"#实际地址
#Location to save the preprocessed training and validation data.
DATA_DIR="${HOME}/model/skip_thoughts/data"
#Build the preprocessing script.
cd tensorflow-models/skip_thoughts
bazel build -c opt //skip_thoughts/data:preprocess_dataset#注意这里是平行相对WORKSPACE地址
source activate tensorflow
bazel-bin/skip_thoughts/data/preprocess_dataset   --input_files=${INPUT_FILES}   --output_dir=${DATA_DIR}#也是相对地址
```
### Run the Training Script
```
# Directory containing the preprocessed data.
DATA_DIR="${HOME}/model/skip_thoughts/data"

# Directory to save the model.
MODEL_DIR="${HOME}/model/skip_thoughts/save_model"

# Build the model.
cd model
bazel build -c opt //skip_thoughts/...#编译BUILD里面所有文件

# Run the training script.#在model（进入有bazel-bin的目录下）
source activate tensorflow
bazel-bin/skip_thoughts/train   --input_file_pattern="${DATA_DIR}/train-?????-of-00100"   --train_dir="${MODEL_DIR}/train"
 ```



