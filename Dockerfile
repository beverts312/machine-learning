FROM beverts312/mlbase

RUN git clone https://github.com/beverts312/dev-env.git &&\
    echo "source /home/mluser/dev-env/setup/my_defaults.sh" >> /home/mluser/.bashrc &&\
    echo "source /home/mluser/dev-env/.bash_profile" >> /home/mluser/.bashrc &&\
    mkdir ./machine-learning &&\
    git clone https://github.com/xinntao/Real-ESRGAN.git esrgan &&\
    git clone https://github.com/gwang-kim/DiffusionCLIP.git diffusion-clip  &&\
    git clone https://github.com/basujindal/stable-diffusion.git &&\
    git clone https://github.com/deforum/stable-diffusion.git deforum

COPY . ./machine-learning

RUN eval "$($CONDA_DIR/bin/conda shell.bash hook)" && \
    cd ./machine-learning &&\
    conda env create -f environment-docker.yaml && \
    conda activate blls

CMD [ "/home/mluser/machine-learning/runpod-start.sh" ]