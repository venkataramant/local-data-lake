FROM apache/hive:4.0.0

USER root
RUN mkdir -p /home/hive/.beeline
RUN chown -R hive:hive /home/hive/.beeline
RUN chmod 755 /home/hive/.beeline
RUN apt-get update
RUN apt-get install -y netcat net-tools curl wget vim

#RUN cp /entrypoint.sh /org_entrypoint.sh
#COPY ./entry_point_local.sh /entry_point_local.sh
#RUN chmod +x /entry_point_local.sh
#RUN chown -R hive:hive  /entry_point_local.sh
#ENTRYPOINT sh -c /entry_point_local.sh
#USER hive
EXPOSE 9083 10000 10001