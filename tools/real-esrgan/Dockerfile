FROM beverts312/machine-learning

RUN git clone https://github.com/xinntao/Real-ESRGAN.git esrgan

WORKDIR /home/mluser/esrgan

RUN pip install basicsr facexlib gfpgan && \
    pip install -r requirements.txt && \
    python setup.py develop

ENTRYPOINT python inference_realesrgan.py -i ../working/input -o ../working/output --fp32
