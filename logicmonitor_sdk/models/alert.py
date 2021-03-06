# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Alert(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource_id': 'int',
        'instance_name': 'str',
        'monitor_object_id': 'int',
        'end_epoch': 'int',
        'rule': 'str',
        'threshold': 'str',
        'type': 'str',
        'start_epoch': 'int',
        'internal_id': 'str',
        'ack_comment': 'str',
        'monitor_object_name': 'str',
        'data_point_name': 'str',
        'instance_id': 'int',
        'data_point_id': 'int',
        'next_recipient': 'int',
        'id': 'str',
        'detail_message': 'object',
        'rule_id': 'int',
        'alert_value': 'str',
        'acked_by': 'str',
        'severity': 'int',
        'sdted': 'bool',
        'acked_epoch': 'int',
        'chain': 'str',
        'sdt': 'object',
        'sub_chain_id': 'int',
        'received_list': 'str',
        'monitor_object_type': 'str',
        'custom_columns': 'object',
        'acked': 'bool',
        'resource_template_type': 'str',
        'clear_value': 'str',
        'instance_description': 'str',
        'monitor_object_groups': 'object',
        'chain_id': 'int',
        'resource_template_id': 'int',
        'cleared': 'bool',
        'resource_template_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'instance_name': 'instanceName',
        'monitor_object_id': 'monitorObjectId',
        'end_epoch': 'endEpoch',
        'rule': 'rule',
        'threshold': 'threshold',
        'type': 'type',
        'start_epoch': 'startEpoch',
        'internal_id': 'internalId',
        'ack_comment': 'ackComment',
        'monitor_object_name': 'monitorObjectName',
        'data_point_name': 'dataPointName',
        'instance_id': 'instanceId',
        'data_point_id': 'dataPointId',
        'next_recipient': 'nextRecipient',
        'id': 'id',
        'detail_message': 'detailMessage',
        'rule_id': 'ruleId',
        'alert_value': 'alertValue',
        'acked_by': 'ackedBy',
        'severity': 'severity',
        'sdted': 'sdted',
        'acked_epoch': 'ackedEpoch',
        'chain': 'chain',
        'sdt': 'SDT',
        'sub_chain_id': 'subChainId',
        'received_list': 'receivedList',
        'monitor_object_type': 'monitorObjectType',
        'custom_columns': 'customColumns',
        'acked': 'acked',
        'resource_template_type': 'resourceTemplateType',
        'clear_value': 'clearValue',
        'instance_description': 'instanceDescription',
        'monitor_object_groups': 'monitorObjectGroups',
        'chain_id': 'chainId',
        'resource_template_id': 'resourceTemplateId',
        'cleared': 'cleared',
        'resource_template_name': 'resourceTemplateName'
    }

    def __init__(self, resource_id=None, instance_name=None, monitor_object_id=None, end_epoch=None, rule=None, threshold=None, type=None, start_epoch=None, internal_id=None, ack_comment=None, monitor_object_name=None, data_point_name=None, instance_id=None, data_point_id=None, next_recipient=None, id=None, detail_message=None, rule_id=None, alert_value=None, acked_by=None, severity=None, sdted=None, acked_epoch=None, chain=None, sdt=None, sub_chain_id=None, received_list=None, monitor_object_type=None, custom_columns=None, acked=None, resource_template_type=None, clear_value=None, instance_description=None, monitor_object_groups=None, chain_id=None, resource_template_id=None, cleared=None, resource_template_name=None):  # noqa: E501
        """Alert - a model defined in Swagger"""  # noqa: E501

        self._resource_id = None
        self._instance_name = None
        self._monitor_object_id = None
        self._end_epoch = None
        self._rule = None
        self._threshold = None
        self._type = None
        self._start_epoch = None
        self._internal_id = None
        self._ack_comment = None
        self._monitor_object_name = None
        self._data_point_name = None
        self._instance_id = None
        self._data_point_id = None
        self._next_recipient = None
        self._id = None
        self._detail_message = None
        self._rule_id = None
        self._alert_value = None
        self._acked_by = None
        self._severity = None
        self._sdted = None
        self._acked_epoch = None
        self._chain = None
        self._sdt = None
        self._sub_chain_id = None
        self._received_list = None
        self._monitor_object_type = None
        self._custom_columns = None
        self._acked = None
        self._resource_template_type = None
        self._clear_value = None
        self._instance_description = None
        self._monitor_object_groups = None
        self._chain_id = None
        self._resource_template_id = None
        self._cleared = None
        self._resource_template_name = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if instance_name is not None:
            self.instance_name = instance_name
        if monitor_object_id is not None:
            self.monitor_object_id = monitor_object_id
        if end_epoch is not None:
            self.end_epoch = end_epoch
        if rule is not None:
            self.rule = rule
        if threshold is not None:
            self.threshold = threshold
        if type is not None:
            self.type = type
        if start_epoch is not None:
            self.start_epoch = start_epoch
        if internal_id is not None:
            self.internal_id = internal_id
        if ack_comment is not None:
            self.ack_comment = ack_comment
        if monitor_object_name is not None:
            self.monitor_object_name = monitor_object_name
        if data_point_name is not None:
            self.data_point_name = data_point_name
        if instance_id is not None:
            self.instance_id = instance_id
        if data_point_id is not None:
            self.data_point_id = data_point_id
        if next_recipient is not None:
            self.next_recipient = next_recipient
        if id is not None:
            self.id = id
        if detail_message is not None:
            self.detail_message = detail_message
        if rule_id is not None:
            self.rule_id = rule_id
        if alert_value is not None:
            self.alert_value = alert_value
        if acked_by is not None:
            self.acked_by = acked_by
        if severity is not None:
            self.severity = severity
        if sdted is not None:
            self.sdted = sdted
        if acked_epoch is not None:
            self.acked_epoch = acked_epoch
        if chain is not None:
            self.chain = chain
        if sdt is not None:
            self.sdt = sdt
        if sub_chain_id is not None:
            self.sub_chain_id = sub_chain_id
        if received_list is not None:
            self.received_list = received_list
        if monitor_object_type is not None:
            self.monitor_object_type = monitor_object_type
        if custom_columns is not None:
            self.custom_columns = custom_columns
        if acked is not None:
            self.acked = acked
        if resource_template_type is not None:
            self.resource_template_type = resource_template_type
        if clear_value is not None:
            self.clear_value = clear_value
        if instance_description is not None:
            self.instance_description = instance_description
        if monitor_object_groups is not None:
            self.monitor_object_groups = monitor_object_groups
        if chain_id is not None:
            self.chain_id = chain_id
        if resource_template_id is not None:
            self.resource_template_id = resource_template_id
        if cleared is not None:
            self.cleared = cleared
        if resource_template_name is not None:
            self.resource_template_name = resource_template_name

    @property
    def resource_id(self):
        """Gets the resource_id of this Alert.  # noqa: E501

        The device specific LogicModule Id  # noqa: E501

        :return: The resource_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Alert.

        The device specific LogicModule Id  # noqa: E501

        :param resource_id: The resource_id of this Alert.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def instance_name(self):
        """Gets the instance_name of this Alert.  # noqa: E501

        The name of the instance in alert  # noqa: E501

        :return: The instance_name of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this Alert.

        The name of the instance in alert  # noqa: E501

        :param instance_name: The instance_name of this Alert.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def monitor_object_id(self):
        """Gets the monitor_object_id of this Alert.  # noqa: E501

        The id of the object that the alert is associated with  # noqa: E501

        :return: The monitor_object_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._monitor_object_id

    @monitor_object_id.setter
    def monitor_object_id(self, monitor_object_id):
        """Sets the monitor_object_id of this Alert.

        The id of the object that the alert is associated with  # noqa: E501

        :param monitor_object_id: The monitor_object_id of this Alert.  # noqa: E501
        :type: int
        """

        self._monitor_object_id = monitor_object_id

    @property
    def end_epoch(self):
        """Gets the end_epoch of this Alert.  # noqa: E501

        The time (in epoch format) that the alert ended  # noqa: E501

        :return: The end_epoch of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._end_epoch

    @end_epoch.setter
    def end_epoch(self, end_epoch):
        """Sets the end_epoch of this Alert.

        The time (in epoch format) that the alert ended  # noqa: E501

        :param end_epoch: The end_epoch of this Alert.  # noqa: E501
        :type: int
        """

        self._end_epoch = end_epoch

    @property
    def rule(self):
        """Gets the rule of this Alert.  # noqa: E501

        The rule the alert matches  # noqa: E501

        :return: The rule of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this Alert.

        The rule the alert matches  # noqa: E501

        :param rule: The rule of this Alert.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def threshold(self):
        """Gets the threshold of this Alert.  # noqa: E501

        The threshold associated with the object in alert  # noqa: E501

        :return: The threshold of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this Alert.

        The threshold associated with the object in alert  # noqa: E501

        :param threshold: The threshold of this Alert.  # noqa: E501
        :type: str
        """

        self._threshold = threshold

    @property
    def type(self):
        """Gets the type of this Alert.  # noqa: E501

        The type of alert  # noqa: E501

        :return: The type of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Alert.

        The type of alert  # noqa: E501

        :param type: The type of this Alert.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def start_epoch(self):
        """Gets the start_epoch of this Alert.  # noqa: E501

        The time (in epoch format) that the alert started  # noqa: E501

        :return: The start_epoch of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._start_epoch

    @start_epoch.setter
    def start_epoch(self, start_epoch):
        """Sets the start_epoch of this Alert.

        The time (in epoch format) that the alert started  # noqa: E501

        :param start_epoch: The start_epoch of this Alert.  # noqa: E501
        :type: int
        """

        self._start_epoch = start_epoch

    @property
    def internal_id(self):
        """Gets the internal_id of this Alert.  # noqa: E501

        The internal id for the alert  # noqa: E501

        :return: The internal_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this Alert.

        The internal id for the alert  # noqa: E501

        :param internal_id: The internal_id of this Alert.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def ack_comment(self):
        """Gets the ack_comment of this Alert.  # noqa: E501

        The comment submitted with the acknowledgement  # noqa: E501

        :return: The ack_comment of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._ack_comment

    @ack_comment.setter
    def ack_comment(self, ack_comment):
        """Sets the ack_comment of this Alert.

        The comment submitted with the acknowledgement  # noqa: E501

        :param ack_comment: The ack_comment of this Alert.  # noqa: E501
        :type: str
        """

        self._ack_comment = ack_comment

    @property
    def monitor_object_name(self):
        """Gets the monitor_object_name of this Alert.  # noqa: E501

        The name of the object that the alert is associated with  # noqa: E501

        :return: The monitor_object_name of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._monitor_object_name

    @monitor_object_name.setter
    def monitor_object_name(self, monitor_object_name):
        """Sets the monitor_object_name of this Alert.

        The name of the object that the alert is associated with  # noqa: E501

        :param monitor_object_name: The monitor_object_name of this Alert.  # noqa: E501
        :type: str
        """

        self._monitor_object_name = monitor_object_name

    @property
    def data_point_name(self):
        """Gets the data_point_name of this Alert.  # noqa: E501

        The name of the datapoint in alert  # noqa: E501

        :return: The data_point_name of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this Alert.

        The name of the datapoint in alert  # noqa: E501

        :param data_point_name: The data_point_name of this Alert.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def instance_id(self):
        """Gets the instance_id of this Alert.  # noqa: E501

        The id of the instance in alert  # noqa: E501

        :return: The instance_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Alert.

        The id of the instance in alert  # noqa: E501

        :param instance_id: The instance_id of this Alert.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def data_point_id(self):
        """Gets the data_point_id of this Alert.  # noqa: E501

        The id of the datapoint in alert  # noqa: E501

        :return: The data_point_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this Alert.

        The id of the datapoint in alert  # noqa: E501

        :param data_point_id: The data_point_id of this Alert.  # noqa: E501
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def next_recipient(self):
        """Gets the next_recipient of this Alert.  # noqa: E501

        The next recipient in the escalation chain for this alert  # noqa: E501

        :return: The next_recipient of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._next_recipient

    @next_recipient.setter
    def next_recipient(self, next_recipient):
        """Sets the next_recipient of this Alert.

        The next recipient in the escalation chain for this alert  # noqa: E501

        :param next_recipient: The next_recipient of this Alert.  # noqa: E501
        :type: int
        """

        self._next_recipient = next_recipient

    @property
    def id(self):
        """Gets the id of this Alert.  # noqa: E501

        The alert id  # noqa: E501

        :return: The id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alert.

        The alert id  # noqa: E501

        :param id: The id of this Alert.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def detail_message(self):
        """Gets the detail_message of this Alert.  # noqa: E501

        The alert message, if needMessage=true is included in the query parameters  # noqa: E501

        :return: The detail_message of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._detail_message

    @detail_message.setter
    def detail_message(self, detail_message):
        """Sets the detail_message of this Alert.

        The alert message, if needMessage=true is included in the query parameters  # noqa: E501

        :param detail_message: The detail_message of this Alert.  # noqa: E501
        :type: object
        """

        self._detail_message = detail_message

    @property
    def rule_id(self):
        """Gets the rule_id of this Alert.  # noqa: E501

        The id of the rule the alert matches  # noqa: E501

        :return: The rule_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this Alert.

        The id of the rule the alert matches  # noqa: E501

        :param rule_id: The rule_id of this Alert.  # noqa: E501
        :type: int
        """

        self._rule_id = rule_id

    @property
    def alert_value(self):
        """Gets the alert_value of this Alert.  # noqa: E501

        The value that triggered the alert  # noqa: E501

        :return: The alert_value of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._alert_value

    @alert_value.setter
    def alert_value(self, alert_value):
        """Sets the alert_value of this Alert.

        The value that triggered the alert  # noqa: E501

        :param alert_value: The alert_value of this Alert.  # noqa: E501
        :type: str
        """

        self._alert_value = alert_value

    @property
    def acked_by(self):
        """Gets the acked_by of this Alert.  # noqa: E501

        The user that acknowledged the alert  # noqa: E501

        :return: The acked_by of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._acked_by

    @acked_by.setter
    def acked_by(self, acked_by):
        """Sets the acked_by of this Alert.

        The user that acknowledged the alert  # noqa: E501

        :param acked_by: The acked_by of this Alert.  # noqa: E501
        :type: str
        """

        self._acked_by = acked_by

    @property
    def severity(self):
        """Gets the severity of this Alert.  # noqa: E501

        The alert severity, where 2=warning, 3=error and 4=critical  # noqa: E501

        :return: The severity of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Alert.

        The alert severity, where 2=warning, 3=error and 4=critical  # noqa: E501

        :param severity: The severity of this Alert.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def sdted(self):
        """Gets the sdted of this Alert.  # noqa: E501

        Whether or not the alert was triggered during an SDT  # noqa: E501

        :return: The sdted of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._sdted

    @sdted.setter
    def sdted(self, sdted):
        """Sets the sdted of this Alert.

        Whether or not the alert was triggered during an SDT  # noqa: E501

        :param sdted: The sdted of this Alert.  # noqa: E501
        :type: bool
        """

        self._sdted = sdted

    @property
    def acked_epoch(self):
        """Gets the acked_epoch of this Alert.  # noqa: E501

        The time (in epoch format) that the alert was acknowledged  # noqa: E501

        :return: The acked_epoch of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._acked_epoch

    @acked_epoch.setter
    def acked_epoch(self, acked_epoch):
        """Sets the acked_epoch of this Alert.

        The time (in epoch format) that the alert was acknowledged  # noqa: E501

        :param acked_epoch: The acked_epoch of this Alert.  # noqa: E501
        :type: int
        """

        self._acked_epoch = acked_epoch

    @property
    def chain(self):
        """Gets the chain of this Alert.  # noqa: E501

        The escalation chain the alert was routed to  # noqa: E501

        :return: The chain of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this Alert.

        The escalation chain the alert was routed to  # noqa: E501

        :param chain: The chain of this Alert.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def sdt(self):
        """Gets the sdt of this Alert.  # noqa: E501

        The active SDT, if one exists  # noqa: E501

        :return: The sdt of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._sdt

    @sdt.setter
    def sdt(self, sdt):
        """Sets the sdt of this Alert.

        The active SDT, if one exists  # noqa: E501

        :param sdt: The sdt of this Alert.  # noqa: E501
        :type: object
        """

        self._sdt = sdt

    @property
    def sub_chain_id(self):
        """Gets the sub_chain_id of this Alert.  # noqa: E501

        The id of the sub time based chain  # noqa: E501

        :return: The sub_chain_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._sub_chain_id

    @sub_chain_id.setter
    def sub_chain_id(self, sub_chain_id):
        """Sets the sub_chain_id of this Alert.

        The id of the sub time based chain  # noqa: E501

        :param sub_chain_id: The sub_chain_id of this Alert.  # noqa: E501
        :type: int
        """

        self._sub_chain_id = sub_chain_id

    @property
    def received_list(self):
        """Gets the received_list of this Alert.  # noqa: E501

        The recipients that have received the alert  # noqa: E501

        :return: The received_list of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._received_list

    @received_list.setter
    def received_list(self, received_list):
        """Sets the received_list of this Alert.

        The recipients that have received the alert  # noqa: E501

        :param received_list: The received_list of this Alert.  # noqa: E501
        :type: str
        """

        self._received_list = received_list

    @property
    def monitor_object_type(self):
        """Gets the monitor_object_type of this Alert.  # noqa: E501


        :return: The monitor_object_type of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._monitor_object_type

    @monitor_object_type.setter
    def monitor_object_type(self, monitor_object_type):
        """Sets the monitor_object_type of this Alert.


        :param monitor_object_type: The monitor_object_type of this Alert.  # noqa: E501
        :type: str
        """

        self._monitor_object_type = monitor_object_type

    @property
    def custom_columns(self):
        """Gets the custom_columns of this Alert.  # noqa: E501

        The property or token values that should display with the alert details. Note that if referencing tokens, you'll need to URL encode the # symbol.  # noqa: E501

        :return: The custom_columns of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._custom_columns

    @custom_columns.setter
    def custom_columns(self, custom_columns):
        """Sets the custom_columns of this Alert.

        The property or token values that should display with the alert details. Note that if referencing tokens, you'll need to URL encode the # symbol.  # noqa: E501

        :param custom_columns: The custom_columns of this Alert.  # noqa: E501
        :type: object
        """

        self._custom_columns = custom_columns

    @property
    def acked(self):
        """Gets the acked of this Alert.  # noqa: E501

        Whether or not the alert has been acknowledged  # noqa: E501

        :return: The acked of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._acked

    @acked.setter
    def acked(self, acked):
        """Sets the acked of this Alert.

        Whether or not the alert has been acknowledged  # noqa: E501

        :param acked: The acked of this Alert.  # noqa: E501
        :type: bool
        """

        self._acked = acked

    @property
    def resource_template_type(self):
        """Gets the resource_template_type of this Alert.  # noqa: E501

        The type of the logicmodule in alert  # noqa: E501

        :return: The resource_template_type of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._resource_template_type

    @resource_template_type.setter
    def resource_template_type(self, resource_template_type):
        """Sets the resource_template_type of this Alert.

        The type of the logicmodule in alert  # noqa: E501

        :param resource_template_type: The resource_template_type of this Alert.  # noqa: E501
        :type: str
        """

        self._resource_template_type = resource_template_type

    @property
    def clear_value(self):
        """Gets the clear_value of this Alert.  # noqa: E501

        The value that cleared the alert  # noqa: E501

        :return: The clear_value of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._clear_value

    @clear_value.setter
    def clear_value(self, clear_value):
        """Sets the clear_value of this Alert.

        The value that cleared the alert  # noqa: E501

        :param clear_value: The clear_value of this Alert.  # noqa: E501
        :type: str
        """

        self._clear_value = clear_value

    @property
    def instance_description(self):
        """Gets the instance_description of this Alert.  # noqa: E501

        The description of the instance in alert  # noqa: E501

        :return: The instance_description of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this Alert.

        The description of the instance in alert  # noqa: E501

        :param instance_description: The instance_description of this Alert.  # noqa: E501
        :type: str
        """

        self._instance_description = instance_description

    @property
    def monitor_object_groups(self):
        """Gets the monitor_object_groups of this Alert.  # noqa: E501

        Information about the groups the object is a member of  # noqa: E501

        :return: The monitor_object_groups of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._monitor_object_groups

    @monitor_object_groups.setter
    def monitor_object_groups(self, monitor_object_groups):
        """Sets the monitor_object_groups of this Alert.

        Information about the groups the object is a member of  # noqa: E501

        :param monitor_object_groups: The monitor_object_groups of this Alert.  # noqa: E501
        :type: object
        """

        self._monitor_object_groups = monitor_object_groups

    @property
    def chain_id(self):
        """Gets the chain_id of this Alert.  # noqa: E501

        The id of the escalation chain the alert was routed to  # noqa: E501

        :return: The chain_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this Alert.

        The id of the escalation chain the alert was routed to  # noqa: E501

        :param chain_id: The chain_id of this Alert.  # noqa: E501
        :type: int
        """

        self._chain_id = chain_id

    @property
    def resource_template_id(self):
        """Gets the resource_template_id of this Alert.  # noqa: E501

        The id of the datasource in alert  # noqa: E501

        :return: The resource_template_id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._resource_template_id

    @resource_template_id.setter
    def resource_template_id(self, resource_template_id):
        """Sets the resource_template_id of this Alert.

        The id of the datasource in alert  # noqa: E501

        :param resource_template_id: The resource_template_id of this Alert.  # noqa: E501
        :type: int
        """

        self._resource_template_id = resource_template_id

    @property
    def cleared(self):
        """Gets the cleared of this Alert.  # noqa: E501

        Whether or not the alert has cleared  # noqa: E501

        :return: The cleared of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this Alert.

        Whether or not the alert has cleared  # noqa: E501

        :param cleared: The cleared of this Alert.  # noqa: E501
        :type: bool
        """

        self._cleared = cleared

    @property
    def resource_template_name(self):
        """Gets the resource_template_name of this Alert.  # noqa: E501

        The name of the datasource in alert  # noqa: E501

        :return: The resource_template_name of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._resource_template_name

    @resource_template_name.setter
    def resource_template_name(self, resource_template_name):
        """Sets the resource_template_name of this Alert.

        The name of the datasource in alert  # noqa: E501

        :param resource_template_name: The resource_template_name of this Alert.  # noqa: E501
        :type: str
        """

        self._resource_template_name = resource_template_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Alert, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
