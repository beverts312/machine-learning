FROM beverts312/mlbase

USER mluser

RUN git clone https://github.com/google-research/maxim.git

WORKDIR /home/mluser/maxim

RUN pip install -r requirements.txt && \
    pip install .

COPY entrypoint.sh .

RUN conda install cudnn

RUN conda install conda-forge

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$CONDA_DIR/lib/

ENTRYPOINT ["./entrypoint.sh"]