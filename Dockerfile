FROM beverts312/mlbase

RUN conda install --yes \
    -c pytorch \
    torchvision=0.14.0 \
    torchaudio \
    pytorch-cuda=11.7 \
    cudatoolkit \
    -c nvidia
