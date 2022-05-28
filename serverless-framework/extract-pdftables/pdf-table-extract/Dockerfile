FROM public.ecr.aws/lambda/python:3.9-x86_64
RUN yum install -y java-17-amazon-corretto
COPY requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt
RUN pip3 install -r ${LAMBDA_TASK_ROOT}/requirements.txt
COPY . ${LAMBDA_TASK_ROOT}
CMD [ "main.lambda_handler" ]
