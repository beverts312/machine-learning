FROM beverts312/mlbase

RUN git clone https://github.com/google-research/maxim.git

WORKDIR /home/mluser/maxim

RUN conda install --yes -c conda-forge \
        cudatoolkit-dev=11.3.1 \
        cudnn  && \
    pip install -U jaxlib==0.3.24+cuda11.cudnn82 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    pip install -r requirements.txt && \
    pip install . 


ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_DIR/lib/:/usr/local/cuda/lib64/

COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
