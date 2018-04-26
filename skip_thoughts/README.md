#安装bazelhttps://docs.bazel.build/versions/master/install-ubuntu.html#install-with-installer-ubuntu<br>
Step 1: Download Bazel<br>
proxychains wget https://github.com/bazelbuild/bazel/releases/download/0.12.0/bazel-0.12.0-installer-linux-x86_64.sh<br>
Step 2: Run the installer<br>
chmod +x bazel-<version>-installer-linux-x86_64.sh<br>
./bazel-<version>-installer-linux-x86_64.sh --user<br>
##The --user flag installs Bazel to the $HOME/bin directory on your system and sets the .bazelrc path to $HOME/.bazelrc. Use the --help command to see additional installation options.##<br>
#source /home/qiujie/.bazel/bin/bazel-complete.bash 这句话加到～/.bashrc可以试试#<br>
Step 3: Set up your environment<br>
##If you ran the Bazel installer with the --user flag as above, the Bazel executable is installed in your $HOME/bin directory. It's a good idea to add this directory to your default paths, as follows:##<br>
export PATH="$PATH:$HOME/bin"##必须有才可以##<br>
Step 4:<br>
source ~/.bashrc<br>

开始：引用https://github.com/tensorflow/models/tree/master/research/skip_thoughts<br>
### 1Prepare the Training Data<br>
#each sentence is already tokenized.<br>
INPUT_FILES="${HOME}/model/skip_thoughts/bookcorpus/*.txt"#实际地址<br>
#Location to save the preprocessed training and validation data.<br>
DATA_DIR="${HOME}/model/skip_thoughts/data"<br>
#Build the preprocessing script.<br>
cd tensorflow-models/skip_thoughts<br>
bazel build -c opt //skip_thoughts/data:preprocess_dataset#注意这里是相对WORKSPACE地址<br>
source activate tensorflow<br>
bazel-bin/skip_thoughts/data/preprocess_dataset   --input_files=${INPUT_FILES}   --output_dir=${DATA_DIR}#也是相对地址<br>



