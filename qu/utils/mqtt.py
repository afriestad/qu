import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe


def publish_mqtt_message(topic, hostname="localhost", port=1883, payload=None, qos=0, retain=None, will=None):
    publish.single(topic=topic, payload=payload, qos=qos, retain=retain, hostname=hostname, port=port, will=will)


def publish_mqtt_messages(msgs, hostname="localhost", port=1883, will=None):
    """
    Publish several mqtt messages at once
    
    :param msgs: 
    a list of messages to publish. Each message is either a dict or a tuple.
    If a dict, only the topic must be present. Default values will be used for any missing arguments. The dict must
    be of the form:
    msg = {'topic':"<topic>", 'payload':"<payload>", 'qos':<qos>, 'retain':<retain>}
    topic must be present and may not be empty. If payload is "", None or not present then a zero length payload will
    be published. If qos is not present, the default of 0 is used. If retain is not present, the default of False is used.
    If a tuple, then it must be of the form:
    ("<topic>", "<payload>", qos, retain)

    :param hostname: 
    :param port: 
    :param will: 
    :return: None
    """
    publish.multiple(msgs=msgs, hostname=hostname, port=port, will=will)


def subscribe_to_topic_with_callback(callback, topics, qos=0, userdata=None, hostname="localhost", port=1883, will=None):
    """
    Non-blocking subscription to one or more mqtt topics

    :param callback: A function reference which will be called with each message received
    :param topics:
    :param qos:
    :param userdata:
    :param hostname:
    :param port:
    :param will:
    :return:
    """
    subscribe.callback(callback=callback, topics=topics, qos=qos, userdata=userdata, hostname=hostname, port=port, will=will)
