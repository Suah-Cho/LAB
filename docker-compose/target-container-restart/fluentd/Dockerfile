FROM fluent/fluentd:edge-debian
USER root
COPY fluentd.conf /fluentd/etc/
RUN mkdir -p /var/pos/ && chmod -R 777 /var/pos/
CMD ["fluentd", "-c", "/fluentd/etc/fluentd.conf"]
EXPOSE 24224