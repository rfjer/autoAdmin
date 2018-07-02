# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models


class Acknowledges(models.Model):
    acknowledgeid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid')
    clock = models.IntegerField()
    message = models.CharField(max_length=255)
    action = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acknowledges'


class Actions(models.Model):
    actionid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    eventsource = models.IntegerField()
    evaltype = models.IntegerField()
    status = models.IntegerField()
    esc_period = models.CharField(max_length=255)
    def_shortdata = models.CharField(max_length=255)
    def_longdata = models.TextField()
    r_shortdata = models.CharField(max_length=255)
    r_longdata = models.TextField()
    formula = models.CharField(max_length=255)
    maintenance_mode = models.IntegerField()
    ack_shortdata = models.CharField(max_length=255)
    ack_longdata = models.TextField()

    class Meta:
        managed = False
        db_table = 'actions'


class Alerts(models.Model):
    alertid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actionid')
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid', related_name="alerts")
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    clock = models.IntegerField()
    mediatypeid = models.ForeignKey('MediaType', models.DO_NOTHING, db_column='mediatypeid', blank=True, null=True)
    sendto = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField()
    retries = models.IntegerField()
    error = models.CharField(max_length=2048)
    esc_step = models.IntegerField()
    alerttype = models.IntegerField()
    p_eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='p_eventid', blank=True, null=True, related_name="p_alerts")
    acknowledgeid = models.ForeignKey(Acknowledges, models.DO_NOTHING, db_column='acknowledgeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alerts'


class ApplicationDiscovery(models.Model):
    application_discoveryid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey('Applications', models.DO_NOTHING, db_column='applicationid')
    application_prototypeid = models.ForeignKey('ApplicationPrototype', models.DO_NOTHING, db_column='application_prototypeid')
    name = models.CharField(max_length=255)
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'application_discovery'


class ApplicationPrototype(models.Model):
    application_prototypeid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'application_prototype'


class ApplicationTemplate(models.Model):
    application_templateid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey('Applications', models.DO_NOTHING, db_column='applicationid', related_name="application")
    templateid = models.ForeignKey('Applications', models.DO_NOTHING, db_column='templateid', related_name="template")

    class Meta:
        managed = False
        db_table = 'application_template'
        unique_together = (('applicationid', 'templateid'),)


class Applications(models.Model):
    applicationid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='hostid')
    name = models.CharField(max_length=255)
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('hostid', 'name'),)


class Auditlog(models.Model):
    auditid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    clock = models.IntegerField()
    action = models.IntegerField()
    resourcetype = models.IntegerField()
    details = models.CharField(max_length=128)
    ip = models.CharField(max_length=39)
    resourceid = models.BigIntegerField()
    resourcename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auditlog'


class AuditlogDetails(models.Model):
    auditdetailid = models.BigIntegerField(primary_key=True)
    auditid = models.ForeignKey(Auditlog, models.DO_NOTHING, db_column='auditid')
    table_name = models.CharField(max_length=64)
    field_name = models.CharField(max_length=64)
    oldvalue = models.TextField()
    newvalue = models.TextField()

    class Meta:
        managed = False
        db_table = 'auditlog_details'


class AutoregHost(models.Model):
    autoreg_hostid = models.BigIntegerField(primary_key=True)
    proxy_hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='proxy_hostid', blank=True, null=True)
    host = models.CharField(max_length=64)
    listen_ip = models.CharField(max_length=39)
    listen_port = models.IntegerField()
    listen_dns = models.CharField(max_length=64)
    host_metadata = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'autoreg_host'


class Conditions(models.Model):
    conditionid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actionid')
    conditiontype = models.IntegerField()
    operator = models.IntegerField()
    value = models.CharField(max_length=255)
    value2 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conditions'


class Config(models.Model):
    configid = models.BigIntegerField(primary_key=True)
    refresh_unsupported = models.CharField(max_length=32)
    work_period = models.CharField(max_length=255)
    alert_usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='alert_usrgrpid', blank=True, null=True)
    event_ack_enable = models.IntegerField()
    event_expire = models.CharField(max_length=32)
    event_show_max = models.IntegerField()
    default_theme = models.CharField(max_length=128)
    authentication_type = models.IntegerField()
    ldap_host = models.CharField(max_length=255)
    ldap_port = models.IntegerField()
    ldap_base_dn = models.CharField(max_length=255)
    ldap_bind_dn = models.CharField(max_length=255)
    ldap_bind_password = models.CharField(max_length=128)
    ldap_search_attribute = models.CharField(max_length=128)
    dropdown_first_entry = models.IntegerField()
    dropdown_first_remember = models.IntegerField()
    discovery_groupid = models.ForeignKey('Groups', models.DO_NOTHING, db_column='discovery_groupid')
    max_in_table = models.IntegerField()
    search_limit = models.IntegerField()
    severity_color_0 = models.CharField(max_length=6)
    severity_color_1 = models.CharField(max_length=6)
    severity_color_2 = models.CharField(max_length=6)
    severity_color_3 = models.CharField(max_length=6)
    severity_color_4 = models.CharField(max_length=6)
    severity_color_5 = models.CharField(max_length=6)
    severity_name_0 = models.CharField(max_length=32)
    severity_name_1 = models.CharField(max_length=32)
    severity_name_2 = models.CharField(max_length=32)
    severity_name_3 = models.CharField(max_length=32)
    severity_name_4 = models.CharField(max_length=32)
    severity_name_5 = models.CharField(max_length=32)
    ok_period = models.CharField(max_length=32)
    blink_period = models.CharField(max_length=32)
    problem_unack_color = models.CharField(max_length=6)
    problem_ack_color = models.CharField(max_length=6)
    ok_unack_color = models.CharField(max_length=6)
    ok_ack_color = models.CharField(max_length=6)
    problem_unack_style = models.IntegerField()
    problem_ack_style = models.IntegerField()
    ok_unack_style = models.IntegerField()
    ok_ack_style = models.IntegerField()
    snmptrap_logging = models.IntegerField()
    server_check_interval = models.IntegerField()
    hk_events_mode = models.IntegerField()
    hk_events_trigger = models.CharField(max_length=32)
    hk_events_internal = models.CharField(max_length=32)
    hk_events_discovery = models.CharField(max_length=32)
    hk_events_autoreg = models.CharField(max_length=32)
    hk_services_mode = models.IntegerField()
    hk_services = models.CharField(max_length=32)
    hk_audit_mode = models.IntegerField()
    hk_audit = models.CharField(max_length=32)
    hk_sessions_mode = models.IntegerField()
    hk_sessions = models.CharField(max_length=32)
    hk_history_mode = models.IntegerField()
    hk_history_global = models.IntegerField()
    hk_history = models.CharField(max_length=32)
    hk_trends_mode = models.IntegerField()
    hk_trends_global = models.IntegerField()
    hk_trends = models.CharField(max_length=32)
    default_inventory_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'config'


class CorrCondition(models.Model):
    corr_conditionid = models.BigIntegerField(primary_key=True)
    correlationid = models.ForeignKey('Correlation', models.DO_NOTHING, db_column='correlationid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'corr_condition'


class CorrConditionGroup(models.Model):
    corr_conditionid = models.OneToOneField(CorrCondition, models.DO_NOTHING, db_column='corr_conditionid', primary_key=True, unique=True)
    operator = models.IntegerField()
    groupid = models.ForeignKey('Groups', models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'corr_condition_group'


class CorrConditionTag(models.Model):
    corr_conditionid = models.OneToOneField(CorrCondition, models.DO_NOTHING, db_column='corr_conditionid', primary_key=True)
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corr_condition_tag'


class CorrConditionTagpair(models.Model):
    corr_conditionid = models.OneToOneField(CorrCondition, models.DO_NOTHING, db_column='corr_conditionid', primary_key=True)
    oldtag = models.CharField(max_length=255)
    newtag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corr_condition_tagpair'


class CorrConditionTagvalue(models.Model):
    corr_conditionid = models.OneToOneField(CorrCondition, models.DO_NOTHING, db_column='corr_conditionid', primary_key=True)
    tag = models.CharField(max_length=255)
    operator = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corr_condition_tagvalue'


class CorrOperation(models.Model):
    corr_operationid = models.BigIntegerField(primary_key=True)
    correlationid = models.ForeignKey('Correlation', models.DO_NOTHING, db_column='correlationid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'corr_operation'


class Correlation(models.Model):
    correlationid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    evaltype = models.IntegerField()
    status = models.IntegerField()
    formula = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'correlation'


class Dashboard(models.Model):
    dashboardid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dashboard'


class DashboardUser(models.Model):
    dashboard_userid = models.BigIntegerField(primary_key=True)
    dashboardid = models.ForeignKey(Dashboard, models.DO_NOTHING, db_column='dashboardid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dashboard_user'
        unique_together = (('dashboardid', 'userid'),)


class DashboardUsrgrp(models.Model):
    dashboard_usrgrpid = models.BigIntegerField(primary_key=True)
    dashboardid = models.ForeignKey(Dashboard, models.DO_NOTHING, db_column='dashboardid')
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dashboard_usrgrp'
        unique_together = (('dashboardid', 'usrgrpid'),)


class Dbversion(models.Model):
    mandatory = models.IntegerField()
    optional = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dbversion'


class Dchecks(models.Model):
    dcheckid = models.BigIntegerField(primary_key=True)
    druleid = models.ForeignKey('Drules', models.DO_NOTHING, db_column='druleid')
    type = models.IntegerField()
    key_field = models.CharField(db_column='key_', max_length=512)  # Field renamed because it ended with '_'.
    snmp_community = models.CharField(max_length=255)
    ports = models.CharField(max_length=255)
    snmpv3_securityname = models.CharField(max_length=64)
    snmpv3_securitylevel = models.IntegerField()
    snmpv3_authpassphrase = models.CharField(max_length=64)
    snmpv3_privpassphrase = models.CharField(max_length=64)
    uniq = models.IntegerField()
    snmpv3_authprotocol = models.IntegerField()
    snmpv3_privprotocol = models.IntegerField()
    snmpv3_contextname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dchecks'


class Dhosts(models.Model):
    dhostid = models.BigIntegerField(primary_key=True)
    druleid = models.ForeignKey('Drules', models.DO_NOTHING, db_column='druleid')
    status = models.IntegerField()
    lastup = models.IntegerField()
    lastdown = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dhosts'


class Drules(models.Model):
    druleid = models.BigIntegerField(primary_key=True)
    proxy_hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='proxy_hostid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    iprange = models.CharField(max_length=2048)
    delay = models.CharField(max_length=255)
    nextcheck = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drules'


class Dservices(models.Model):
    dserviceid = models.BigIntegerField(primary_key=True)
    dhostid = models.ForeignKey(Dhosts, models.DO_NOTHING, db_column='dhostid')
    value = models.CharField(max_length=255)
    port = models.IntegerField()
    status = models.IntegerField()
    lastup = models.IntegerField()
    lastdown = models.IntegerField()
    dcheckid = models.ForeignKey(Dchecks, models.DO_NOTHING, db_column='dcheckid')
    ip = models.CharField(max_length=39)
    dns = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'dservices'
        unique_together = (('dcheckid', 'ip', 'port'),)


class Escalations(models.Model):
    escalationid = models.BigIntegerField(primary_key=True)
    actionid = models.BigIntegerField()
    triggerid = models.BigIntegerField(blank=True, null=True)
    eventid = models.BigIntegerField(blank=True, null=True)
    r_eventid = models.BigIntegerField(blank=True, null=True)
    nextcheck = models.IntegerField()
    esc_step = models.IntegerField()
    status = models.IntegerField()
    itemid = models.BigIntegerField(blank=True, null=True)
    acknowledgeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalations'
        unique_together = (('actionid', 'triggerid', 'itemid', 'escalationid'),)


class EventRecovery(models.Model):
    eventid = models.OneToOneField('Events', models.DO_NOTHING, db_column='eventid', primary_key=True)
    r_eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='r_eventid', related_name="recovery_r_eventid")
    c_eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='c_eventid', blank=True, null=True, related_name="recovery_c_eventid")
    correlationid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_recovery'


class EventTag(models.Model):
    eventtagid = models.BigIntegerField(primary_key=True)
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid')
    tag = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'event_tag'


class Events(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    source = models.IntegerField()
    object = models.IntegerField()
    objectid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.IntegerField()
    acknowledged = models.IntegerField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events'


class Expressions(models.Model):
    expressionid = models.BigIntegerField(primary_key=True)
    regexpid = models.ForeignKey('Regexps', models.DO_NOTHING, db_column='regexpid')
    expression = models.CharField(max_length=255)
    expression_type = models.IntegerField()
    exp_delimiter = models.CharField(max_length=1)
    case_sensitive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expressions'


class Functions(models.Model):
    functionid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid')
    function = models.CharField(max_length=12)
    parameter = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'functions'


class Globalmacro(models.Model):
    globalmacroid = models.BigIntegerField(primary_key=True)
    macro = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'globalmacro'


class Globalvars(models.Model):
    globalvarid = models.BigIntegerField(primary_key=True)
    snmp_lastsize = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'globalvars'


class GraphDiscovery(models.Model):
    graphid = models.OneToOneField('Graphs', models.DO_NOTHING, db_column='graphid', primary_key=True, related_name="discovery_graph")
    parent_graphid = models.ForeignKey('Graphs', models.DO_NOTHING, db_column='parent_graphid', related_name="discovery_parent_graph")

    class Meta:
        managed = False
        db_table = 'graph_discovery'


class GraphTheme(models.Model):
    graphthemeid = models.BigIntegerField(primary_key=True)
    theme = models.CharField(unique=True, max_length=64)
    backgroundcolor = models.CharField(max_length=6)
    graphcolor = models.CharField(max_length=6)
    gridcolor = models.CharField(max_length=6)
    maingridcolor = models.CharField(max_length=6)
    gridbordercolor = models.CharField(max_length=6)
    textcolor = models.CharField(max_length=6)
    highlightcolor = models.CharField(max_length=6)
    leftpercentilecolor = models.CharField(max_length=6)
    rightpercentilecolor = models.CharField(max_length=6)
    nonworktimecolor = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'graph_theme'


class Graphs(models.Model):
    graphid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    width = models.IntegerField()
    height = models.IntegerField()
    yaxismin = models.FloatField()
    yaxismax = models.FloatField()
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    show_work_period = models.IntegerField()
    show_triggers = models.IntegerField()
    graphtype = models.IntegerField()
    show_legend = models.IntegerField()
    show_3d = models.IntegerField()
    percent_left = models.FloatField()
    percent_right = models.FloatField()
    ymin_type = models.IntegerField()
    ymax_type = models.IntegerField()
    ymin_itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ymin_itemid', blank=True, null=True, related_name="ymin_item")
    ymax_itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ymax_itemid', blank=True, null=True, related_name="ymax_item")
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'graphs'


class GraphsItems(models.Model):
    gitemid = models.BigIntegerField(primary_key=True)
    graphid = models.ForeignKey(Graphs, models.DO_NOTHING, db_column='graphid')
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    drawtype = models.IntegerField()
    sortorder = models.IntegerField()
    color = models.CharField(max_length=6)
    yaxisside = models.IntegerField()
    calc_fnc = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'graphs_items'


class GroupDiscovery(models.Model):
    groupid = models.OneToOneField('Groups', models.DO_NOTHING, db_column='groupid', primary_key=True)
    parent_group_prototypeid = models.ForeignKey('GroupPrototype', models.DO_NOTHING, db_column='parent_group_prototypeid')
    name = models.CharField(max_length=64)
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_discovery'


class GroupPrototype(models.Model):
    group_prototypeid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='hostid')
    name = models.CharField(max_length=255)
    groupid = models.ForeignKey('Groups', models.DO_NOTHING, db_column='groupid', blank=True, null=True)
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_prototype'


class Groups(models.Model):
    groupid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    internal = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class History(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.FloatField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history'


class HistoryLog(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    timestamp = models.IntegerField()
    source = models.CharField(max_length=64)
    severity = models.IntegerField()
    value = models.TextField()
    logeventid = models.IntegerField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_log'


class HistoryStr(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.CharField(max_length=255)
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_str'


class HistoryText(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.TextField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_text'


class HistoryUint(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.BigIntegerField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_uint'


class HostDiscovery(models.Model):
    hostid = models.OneToOneField('Hosts', models.DO_NOTHING, db_column='hostid', primary_key=True, related_name="discovery_host")
    parent_hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='parent_hostid', blank=True, null=True, related_name="parent_host")
    parent_itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='parent_itemid', blank=True, null=True)
    host = models.CharField(max_length=64)
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'host_discovery'


class HostInventory(models.Model):
    hostid = models.OneToOneField('Hosts', models.DO_NOTHING, db_column='hostid', primary_key=True)
    inventory_mode = models.IntegerField()
    type = models.CharField(max_length=64)
    type_full = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    os_full = models.CharField(max_length=255)
    os_short = models.CharField(max_length=64)
    serialno_a = models.CharField(max_length=64)
    serialno_b = models.CharField(max_length=64)
    tag = models.CharField(max_length=64)
    asset_tag = models.CharField(max_length=64)
    macaddress_a = models.CharField(max_length=64)
    macaddress_b = models.CharField(max_length=64)
    hardware = models.CharField(max_length=255)
    hardware_full = models.TextField()
    software = models.CharField(max_length=255)
    software_full = models.TextField()
    software_app_a = models.CharField(max_length=64)
    software_app_b = models.CharField(max_length=64)
    software_app_c = models.CharField(max_length=64)
    software_app_d = models.CharField(max_length=64)
    software_app_e = models.CharField(max_length=64)
    contact = models.TextField()
    location = models.TextField()
    location_lat = models.CharField(max_length=16)
    location_lon = models.CharField(max_length=16)
    notes = models.TextField()
    chassis = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    hw_arch = models.CharField(max_length=32)
    vendor = models.CharField(max_length=64)
    contract_number = models.CharField(max_length=64)
    installer_name = models.CharField(max_length=64)
    deployment_status = models.CharField(max_length=64)
    url_a = models.CharField(max_length=255)
    url_b = models.CharField(max_length=255)
    url_c = models.CharField(max_length=255)
    host_networks = models.TextField()
    host_netmask = models.CharField(max_length=39)
    host_router = models.CharField(max_length=39)
    oob_ip = models.CharField(max_length=39)
    oob_netmask = models.CharField(max_length=39)
    oob_router = models.CharField(max_length=39)
    date_hw_purchase = models.CharField(max_length=64)
    date_hw_install = models.CharField(max_length=64)
    date_hw_expiry = models.CharField(max_length=64)
    date_hw_decomm = models.CharField(max_length=64)
    site_address_a = models.CharField(max_length=128)
    site_address_b = models.CharField(max_length=128)
    site_address_c = models.CharField(max_length=128)
    site_city = models.CharField(max_length=128)
    site_state = models.CharField(max_length=64)
    site_country = models.CharField(max_length=64)
    site_zip = models.CharField(max_length=64)
    site_rack = models.CharField(max_length=128)
    site_notes = models.TextField()
    poc_1_name = models.CharField(max_length=128)
    poc_1_email = models.CharField(max_length=128)
    poc_1_phone_a = models.CharField(max_length=64)
    poc_1_phone_b = models.CharField(max_length=64)
    poc_1_cell = models.CharField(max_length=64)
    poc_1_screen = models.CharField(max_length=64)
    poc_1_notes = models.TextField()
    poc_2_name = models.CharField(max_length=128)
    poc_2_email = models.CharField(max_length=128)
    poc_2_phone_a = models.CharField(max_length=64)
    poc_2_phone_b = models.CharField(max_length=64)
    poc_2_cell = models.CharField(max_length=64)
    poc_2_screen = models.CharField(max_length=64)
    poc_2_notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'host_inventory'


class Hostmacro(models.Model):
    hostmacroid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='hostid')
    macro = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hostmacro'
        unique_together = (('hostid', 'macro'),)


class Hosts(models.Model):
    hostid = models.BigIntegerField(primary_key=True)
    proxy_hostid = models.ForeignKey('self', models.DO_NOTHING, db_column='proxy_hostid', blank=True, null=True, related_name="proxy_host")
    host = models.CharField(max_length=128)
    status = models.IntegerField()
    disable_until = models.IntegerField()
    error = models.CharField(max_length=2048)
    available = models.IntegerField()
    errors_from = models.IntegerField()
    lastaccess = models.IntegerField()
    ipmi_authtype = models.IntegerField()
    ipmi_privilege = models.IntegerField()
    ipmi_username = models.CharField(max_length=16)
    ipmi_password = models.CharField(max_length=20)
    ipmi_disable_until = models.IntegerField()
    ipmi_available = models.IntegerField()
    snmp_disable_until = models.IntegerField()
    snmp_available = models.IntegerField()
    maintenanceid = models.ForeignKey('Maintenances', models.DO_NOTHING, db_column='maintenanceid', blank=True, null=True)
    maintenance_status = models.IntegerField()
    maintenance_type = models.IntegerField()
    maintenance_from = models.IntegerField()
    ipmi_errors_from = models.IntegerField()
    snmp_errors_from = models.IntegerField()
    ipmi_error = models.CharField(max_length=2048)
    snmp_error = models.CharField(max_length=2048)
    jmx_disable_until = models.IntegerField()
    jmx_available = models.IntegerField()
    jmx_errors_from = models.IntegerField()
    jmx_error = models.CharField(max_length=2048)
    name = models.CharField(max_length=128)
    flags = models.IntegerField()
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    description = models.TextField()
    tls_connect = models.IntegerField()
    tls_accept = models.IntegerField()
    tls_issuer = models.CharField(max_length=1024)
    tls_subject = models.CharField(max_length=1024)
    tls_psk_identity = models.CharField(max_length=128)
    tls_psk = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'hosts'


class HostsGroups(models.Model):
    hostgroupid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'hosts_groups'
        unique_together = (('hostid', 'groupid'),)


class HostsTemplates(models.Model):
    hosttemplateid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid', related_name="host_template")
    templateid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='templateid')

    class Meta:
        managed = False
        db_table = 'hosts_templates'
        unique_together = (('hostid', 'templateid'),)


class Housekeeper(models.Model):
    housekeeperid = models.BigIntegerField(primary_key=True)
    tablename = models.CharField(max_length=64)
    field = models.CharField(max_length=64)
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'housekeeper'


class Httpstep(models.Model):
    httpstepid = models.BigIntegerField(primary_key=True)
    httptestid = models.ForeignKey('Httptest', models.DO_NOTHING, db_column='httptestid')
    name = models.CharField(max_length=64)
    no = models.IntegerField()
    url = models.CharField(max_length=2048)
    timeout = models.CharField(max_length=255)
    posts = models.TextField()
    required = models.CharField(max_length=255)
    status_codes = models.CharField(max_length=255)
    follow_redirects = models.IntegerField()
    retrieve_mode = models.IntegerField()
    post_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httpstep'


class HttpstepField(models.Model):
    httpstep_fieldid = models.BigIntegerField(primary_key=True)
    httpstepid = models.ForeignKey(Httpstep, models.DO_NOTHING, db_column='httpstepid')
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'httpstep_field'


class Httpstepitem(models.Model):
    httpstepitemid = models.BigIntegerField(primary_key=True)
    httpstepid = models.ForeignKey(Httpstep, models.DO_NOTHING, db_column='httpstepid')
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httpstepitem'
        unique_together = (('httpstepid', 'itemid'),)


class Httptest(models.Model):
    httptestid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    applicationid = models.ForeignKey(Applications, models.DO_NOTHING, db_column='applicationid', blank=True, null=True)
    nextcheck = models.IntegerField()
    delay = models.CharField(max_length=255)
    status = models.IntegerField()
    agent = models.CharField(max_length=255)
    authentication = models.IntegerField()
    http_user = models.CharField(max_length=64)
    http_password = models.CharField(max_length=64)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    http_proxy = models.CharField(max_length=255)
    retries = models.IntegerField()
    ssl_cert_file = models.CharField(max_length=255)
    ssl_key_file = models.CharField(max_length=255)
    ssl_key_password = models.CharField(max_length=64)
    verify_peer = models.IntegerField()
    verify_host = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httptest'
        unique_together = (('hostid', 'name'),)


class HttptestField(models.Model):
    httptest_fieldid = models.BigIntegerField(primary_key=True)
    httptestid = models.ForeignKey(Httptest, models.DO_NOTHING, db_column='httptestid')
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'httptest_field'


class Httptestitem(models.Model):
    httptestitemid = models.BigIntegerField(primary_key=True)
    httptestid = models.ForeignKey(Httptest, models.DO_NOTHING, db_column='httptestid')
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httptestitem'
        unique_together = (('httptestid', 'itemid'),)


class IconMap(models.Model):
    iconmapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    default_iconid = models.ForeignKey('Images', models.DO_NOTHING, db_column='default_iconid')

    class Meta:
        managed = False
        db_table = 'icon_map'


class IconMapping(models.Model):
    iconmappingid = models.BigIntegerField(primary_key=True)
    iconmapid = models.ForeignKey(IconMap, models.DO_NOTHING, db_column='iconmapid')
    iconid = models.ForeignKey('Images', models.DO_NOTHING, db_column='iconid')
    inventory_link = models.IntegerField()
    expression = models.CharField(max_length=64)
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icon_mapping'


class Ids(models.Model):
    table_name = models.CharField(primary_key=True, max_length=64)
    field_name = models.CharField(max_length=64)
    nextid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ids'
        unique_together = (('table_name', 'field_name'),)


class Images(models.Model):
    imageid = models.BigIntegerField(primary_key=True)
    imagetype = models.IntegerField()
    name = models.CharField(unique=True, max_length=64)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'images'


class Interface(models.Model):
    interfaceid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    main = models.IntegerField()
    type = models.IntegerField()
    useip = models.IntegerField()
    ip = models.CharField(max_length=64)
    dns = models.CharField(max_length=64)
    port = models.CharField(max_length=64)
    bulk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interface'


class InterfaceDiscovery(models.Model):
    interfaceid = models.OneToOneField(Interface, models.DO_NOTHING, db_column='interfaceid', primary_key=True, related_name="interface")
    parent_interfaceid = models.ForeignKey(Interface, models.DO_NOTHING, db_column='parent_interfaceid', related_name="parent_interface")

    class Meta:
        managed = False
        db_table = 'interface_discovery'


class ItemApplicationPrototype(models.Model):
    item_application_prototypeid = models.BigIntegerField(primary_key=True)
    application_prototypeid = models.ForeignKey(ApplicationPrototype, models.DO_NOTHING, db_column='application_prototypeid')
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')

    class Meta:
        managed = False
        db_table = 'item_application_prototype'
        unique_together = (('application_prototypeid', 'itemid'),)


class ItemCondition(models.Model):
    item_conditionid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    operator = models.IntegerField()
    macro = models.CharField(max_length=64)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'item_condition'


class ItemDiscovery(models.Model):
    itemdiscoveryid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid', related_name="discovery_item")
    parent_itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='parent_itemid', related_name="discovery_parent_item")
    key_field = models.CharField(db_column='key_', max_length=255)  # Field renamed because it ended with '_'.
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_discovery'
        unique_together = (('itemid', 'parent_itemid'),)


class ItemPreproc(models.Model):
    item_preprocid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemid')
    step = models.IntegerField()
    type = models.IntegerField()
    params = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'item_preproc'


class Items(models.Model):
    itemid = models.BigIntegerField(primary_key=True)
    type = models.IntegerField()
    snmp_community = models.CharField(max_length=64)
    snmp_oid = models.CharField(max_length=512)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    name = models.CharField(max_length=255)
    key_field = models.CharField(db_column='key_', max_length=255)  # Field renamed because it ended with '_'.
    delay = models.CharField(max_length=1024)
    history = models.CharField(max_length=255)
    trends = models.CharField(max_length=255)
    status = models.IntegerField()
    value_type = models.IntegerField()
    trapper_hosts = models.CharField(max_length=255)
    units = models.CharField(max_length=255)
    snmpv3_securityname = models.CharField(max_length=64)
    snmpv3_securitylevel = models.IntegerField()
    snmpv3_authpassphrase = models.CharField(max_length=64)
    snmpv3_privpassphrase = models.CharField(max_length=64)
    formula = models.CharField(max_length=255)
    error = models.CharField(max_length=2048)
    lastlogsize = models.BigIntegerField()
    logtimefmt = models.CharField(max_length=64)
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True, related_name="template_item")
    valuemapid = models.ForeignKey('Valuemaps', models.DO_NOTHING, db_column='valuemapid', blank=True, null=True)
    params = models.TextField()
    ipmi_sensor = models.CharField(max_length=128)
    authtype = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    publickey = models.CharField(max_length=64)
    privatekey = models.CharField(max_length=64)
    mtime = models.IntegerField()
    flags = models.IntegerField()
    interfaceid = models.ForeignKey(Interface, models.DO_NOTHING, db_column='interfaceid', blank=True, null=True)
    port = models.CharField(max_length=64)
    description = models.TextField()
    inventory_link = models.IntegerField()
    lifetime = models.CharField(max_length=255)
    snmpv3_authprotocol = models.IntegerField()
    snmpv3_privprotocol = models.IntegerField()
    state = models.IntegerField()
    snmpv3_contextname = models.CharField(max_length=255)
    evaltype = models.IntegerField()
    jmx_endpoint = models.CharField(max_length=255)
    master_itemid = models.ForeignKey('self', models.DO_NOTHING, db_column='master_itemid', blank=True, null=True, related_name="master_item")

    class Meta:
        managed = False
        db_table = 'items'
        unique_together = (('hostid', 'key_field'),)


class ItemsApplications(models.Model):
    itemappid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey(Applications, models.DO_NOTHING, db_column='applicationid')
    itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemid')

    class Meta:
        managed = False
        db_table = 'items_applications'
        unique_together = (('applicationid', 'itemid'),)


class Maintenances(models.Model):
    maintenanceid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    maintenance_type = models.IntegerField()
    description = models.TextField()
    active_since = models.IntegerField()
    active_till = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenances'


class MaintenancesGroups(models.Model):
    maintenance_groupid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, models.DO_NOTHING, db_column='maintenanceid')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'maintenances_groups'
        unique_together = (('maintenanceid', 'groupid'),)


class MaintenancesHosts(models.Model):
    maintenance_hostid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, models.DO_NOTHING, db_column='maintenanceid')
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')

    class Meta:
        managed = False
        db_table = 'maintenances_hosts'
        unique_together = (('maintenanceid', 'hostid'),)


class MaintenancesWindows(models.Model):
    maintenance_timeperiodid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, models.DO_NOTHING, db_column='maintenanceid')
    timeperiodid = models.ForeignKey('Timeperiods', models.DO_NOTHING, db_column='timeperiodid')

    class Meta:
        managed = False
        db_table = 'maintenances_windows'
        unique_together = (('maintenanceid', 'timeperiodid'),)


class Mappings(models.Model):
    mappingid = models.BigIntegerField(primary_key=True)
    valuemapid = models.ForeignKey('Valuemaps', models.DO_NOTHING, db_column='valuemapid')
    value = models.CharField(max_length=64)
    newvalue = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mappings'


class Media(models.Model):
    mediaid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    mediatypeid = models.ForeignKey('MediaType', models.DO_NOTHING, db_column='mediatypeid')
    sendto = models.CharField(max_length=100)
    active = models.IntegerField()
    severity = models.IntegerField()
    period = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'media'


class MediaType(models.Model):
    mediatypeid = models.BigIntegerField(primary_key=True)
    type = models.IntegerField()
    description = models.CharField(unique=True, max_length=100)
    smtp_server = models.CharField(max_length=255)
    smtp_helo = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    exec_path = models.CharField(max_length=255)
    gsm_modem = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    status = models.IntegerField()
    smtp_port = models.IntegerField()
    smtp_security = models.IntegerField()
    smtp_verify_peer = models.IntegerField()
    smtp_verify_host = models.IntegerField()
    smtp_authentication = models.IntegerField()
    exec_params = models.CharField(max_length=255)
    maxsessions = models.IntegerField()
    maxattempts = models.IntegerField()
    attempt_interval = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'media_type'


class Opcommand(models.Model):
    operationid = models.OneToOneField('Operations', models.DO_NOTHING, db_column='operationid', primary_key=True)
    type = models.IntegerField()
    scriptid = models.ForeignKey('Scripts', models.DO_NOTHING, db_column='scriptid', blank=True, null=True)
    execute_on = models.IntegerField()
    port = models.CharField(max_length=64)
    authtype = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    publickey = models.CharField(max_length=64)
    privatekey = models.CharField(max_length=64)
    command = models.TextField()

    class Meta:
        managed = False
        db_table = 'opcommand'


class OpcommandGrp(models.Model):
    opcommand_grpid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', models.DO_NOTHING, db_column='operationid')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'opcommand_grp'


class OpcommandHst(models.Model):
    opcommand_hstid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', models.DO_NOTHING, db_column='operationid')
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opcommand_hst'


class Opconditions(models.Model):
    opconditionid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', models.DO_NOTHING, db_column='operationid')
    conditiontype = models.IntegerField()
    operator = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'opconditions'


class Operations(models.Model):
    operationid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='actionid')
    operationtype = models.IntegerField()
    esc_period = models.CharField(max_length=255)
    esc_step_from = models.IntegerField()
    esc_step_to = models.IntegerField()
    evaltype = models.IntegerField()
    recovery = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operations'


class Opgroup(models.Model):
    opgroupid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, models.DO_NOTHING, db_column='operationid')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'opgroup'
        unique_together = (('operationid', 'groupid'),)


class Opinventory(models.Model):
    operationid = models.OneToOneField(Operations, models.DO_NOTHING, db_column='operationid', primary_key=True)
    inventory_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'opinventory'


class Opmessage(models.Model):
    operationid = models.OneToOneField(Operations, models.DO_NOTHING, db_column='operationid', primary_key=True)
    default_msg = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    mediatypeid = models.ForeignKey(MediaType, models.DO_NOTHING, db_column='mediatypeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opmessage'


class OpmessageGrp(models.Model):
    opmessage_grpid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, models.DO_NOTHING, db_column='operationid')
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')

    class Meta:
        managed = False
        db_table = 'opmessage_grp'
        unique_together = (('operationid', 'usrgrpid'),)


class OpmessageUsr(models.Model):
    opmessage_usrid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, models.DO_NOTHING, db_column='operationid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'opmessage_usr'
        unique_together = (('operationid', 'userid'),)


class Optemplate(models.Model):
    optemplateid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, models.DO_NOTHING, db_column='operationid')
    templateid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='templateid')

    class Meta:
        managed = False
        db_table = 'optemplate'
        unique_together = (('operationid', 'templateid'),)


class Problem(models.Model):
    eventid = models.OneToOneField(Events, models.DO_NOTHING, db_column='eventid', primary_key=True, related_name="problem_event")
    source = models.IntegerField()
    object = models.IntegerField()
    objectid = models.BigIntegerField()
    clock = models.IntegerField()
    ns = models.IntegerField()
    r_eventid = models.ForeignKey(Events, models.DO_NOTHING, db_column='r_eventid', blank=True, null=True, related_name="problem_r_event")
    r_clock = models.IntegerField()
    r_ns = models.IntegerField()
    correlationid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem'


class ProblemTag(models.Model):
    problemtagid = models.BigIntegerField(primary_key=True)
    eventid = models.ForeignKey(Problem, models.DO_NOTHING, db_column='eventid')
    tag = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'problem_tag'


class Profiles(models.Model):
    profileid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    idx = models.CharField(max_length=96)
    idx2 = models.BigIntegerField()
    value_id = models.BigIntegerField()
    value_int = models.IntegerField()
    value_str = models.CharField(max_length=255)
    source = models.CharField(max_length=96)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profiles'


class ProxyAutoregHost(models.Model):
    id = models.BigAutoField(primary_key=True)
    clock = models.IntegerField()
    host = models.CharField(max_length=64)
    listen_ip = models.CharField(max_length=39)
    listen_port = models.IntegerField()
    listen_dns = models.CharField(max_length=64)
    host_metadata = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'proxy_autoreg_host'


class ProxyDhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    clock = models.IntegerField()
    druleid = models.BigIntegerField()
    ip = models.CharField(max_length=39)
    port = models.IntegerField()
    value = models.CharField(max_length=255)
    status = models.IntegerField()
    dcheckid = models.BigIntegerField(blank=True, null=True)
    dns = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'proxy_dhistory'


class ProxyHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    timestamp = models.IntegerField()
    source = models.CharField(max_length=64)
    severity = models.IntegerField()
    value = models.TextField()
    logeventid = models.IntegerField()
    ns = models.IntegerField()
    state = models.IntegerField()
    lastlogsize = models.BigIntegerField()
    mtime = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proxy_history'


class Regexps(models.Model):
    regexpid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    test_string = models.TextField()

    class Meta:
        managed = False
        db_table = 'regexps'


class Rights(models.Model):
    rightid = models.BigIntegerField(primary_key=True)
    groupid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='groupid')
    permission = models.IntegerField()
    id = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'rights'


class ScreenUser(models.Model):
    screenuserid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey('Screens', models.DO_NOTHING, db_column='screenid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screen_user'
        unique_together = (('screenid', 'userid'),)


class ScreenUsrgrp(models.Model):
    screenusrgrpid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey('Screens', models.DO_NOTHING, db_column='screenid')
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screen_usrgrp'
        unique_together = (('screenid', 'usrgrpid'),)


class Screens(models.Model):
    screenid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    hsize = models.IntegerField()
    vsize = models.IntegerField()
    templateid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screens'


class ScreensItems(models.Model):
    screenitemid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey(Screens, models.DO_NOTHING, db_column='screenid')
    resourcetype = models.IntegerField()
    resourceid = models.BigIntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    colspan = models.IntegerField()
    rowspan = models.IntegerField()
    elements = models.IntegerField()
    valign = models.IntegerField()
    halign = models.IntegerField()
    style = models.IntegerField()
    url = models.CharField(max_length=255)
    dynamic = models.IntegerField()
    sort_triggers = models.IntegerField()
    application = models.CharField(max_length=255)
    max_columns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screens_items'


class Scripts(models.Model):
    scriptid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    command = models.CharField(max_length=255)
    host_access = models.IntegerField()
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid', blank=True, null=True)
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid', blank=True, null=True)
    description = models.TextField()
    confirmation = models.CharField(max_length=255)
    type = models.IntegerField()
    execute_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scripts'


class ServiceAlarms(models.Model):
    servicealarmid = models.BigIntegerField(primary_key=True)
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='serviceid')
    clock = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_alarms'


class Services(models.Model):
    serviceid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    status = models.IntegerField()
    algorithm = models.IntegerField()
    triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid', blank=True, null=True)
    showsla = models.IntegerField()
    goodsla = models.FloatField()
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services'


class ServicesLinks(models.Model):
    linkid = models.BigIntegerField(primary_key=True)
    serviceupid = models.ForeignKey(Services, models.DO_NOTHING, db_column='serviceupid', related_name="service_up_link")
    servicedownid = models.ForeignKey(Services, models.DO_NOTHING, db_column='servicedownid', related_name="service_down_link")
    soft = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_links'
        unique_together = (('serviceupid', 'servicedownid'),)


class ServicesTimes(models.Model):
    timeid = models.BigIntegerField(primary_key=True)
    serviceid = models.ForeignKey(Services, models.DO_NOTHING, db_column='serviceid')
    type = models.IntegerField()
    ts_from = models.IntegerField()
    ts_to = models.IntegerField()
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'services_times'


class Sessions(models.Model):
    sessionid = models.CharField(primary_key=True, max_length=32)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    lastaccess = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Slides(models.Model):
    slideid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', models.DO_NOTHING, db_column='slideshowid')
    screenid = models.ForeignKey(Screens, models.DO_NOTHING, db_column='screenid')
    step = models.IntegerField()
    delay = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'slides'


class SlideshowUser(models.Model):
    slideshowuserid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', models.DO_NOTHING, db_column='slideshowid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshow_user'
        unique_together = (('slideshowid', 'userid'),)


class SlideshowUsrgrp(models.Model):
    slideshowusrgrpid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', models.DO_NOTHING, db_column='slideshowid')
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshow_usrgrp'
        unique_together = (('slideshowid', 'usrgrpid'),)


class Slideshows(models.Model):
    slideshowid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    delay = models.CharField(max_length=32)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshows'


class SysmapElementTrigger(models.Model):
    selement_triggerid = models.BigIntegerField(primary_key=True)
    selementid = models.ForeignKey('SysmapsElements', models.DO_NOTHING, db_column='selementid')
    triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid')

    class Meta:
        managed = False
        db_table = 'sysmap_element_trigger'
        unique_together = (('selementid', 'triggerid'),)


class SysmapElementUrl(models.Model):
    sysmapelementurlid = models.BigIntegerField(primary_key=True)
    selementid = models.ForeignKey('SysmapsElements', models.DO_NOTHING, db_column='selementid')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sysmap_element_url'
        unique_together = (('selementid', 'name'),)


class SysmapShape(models.Model):
    sysmap_shapeid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', models.DO_NOTHING, db_column='sysmapid')
    type = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    text = models.TextField()
    font = models.IntegerField()
    font_size = models.IntegerField()
    font_color = models.CharField(max_length=6)
    text_halign = models.IntegerField()
    text_valign = models.IntegerField()
    border_type = models.IntegerField()
    border_width = models.IntegerField()
    border_color = models.CharField(max_length=6)
    background_color = models.CharField(max_length=6)
    zindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_shape'


class SysmapUrl(models.Model):
    sysmapurlid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', models.DO_NOTHING, db_column='sysmapid')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    elementtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_url'
        unique_together = (('sysmapid', 'name'),)


class SysmapUser(models.Model):
    sysmapuserid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', models.DO_NOTHING, db_column='sysmapid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_user'
        unique_together = (('sysmapid', 'userid'),)


class SysmapUsrgrp(models.Model):
    sysmapusrgrpid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', models.DO_NOTHING, db_column='sysmapid')
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_usrgrp'
        unique_together = (('sysmapid', 'usrgrpid'),)


class Sysmaps(models.Model):
    sysmapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    width = models.IntegerField()
    height = models.IntegerField()
    backgroundid = models.ForeignKey(Images, models.DO_NOTHING, db_column='backgroundid', blank=True, null=True)
    label_type = models.IntegerField()
    label_location = models.IntegerField()
    highlight = models.IntegerField()
    expandproblem = models.IntegerField()
    markelements = models.IntegerField()
    show_unack = models.IntegerField()
    grid_size = models.IntegerField()
    grid_show = models.IntegerField()
    grid_align = models.IntegerField()
    label_format = models.IntegerField()
    label_type_host = models.IntegerField()
    label_type_hostgroup = models.IntegerField()
    label_type_trigger = models.IntegerField()
    label_type_map = models.IntegerField()
    label_type_image = models.IntegerField()
    label_string_host = models.CharField(max_length=255)
    label_string_hostgroup = models.CharField(max_length=255)
    label_string_trigger = models.CharField(max_length=255)
    label_string_map = models.CharField(max_length=255)
    label_string_image = models.CharField(max_length=255)
    iconmapid = models.ForeignKey(IconMap, models.DO_NOTHING, db_column='iconmapid', blank=True, null=True)
    expand_macros = models.IntegerField()
    severity_min = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmaps'


class SysmapsElements(models.Model):
    selementid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey(Sysmaps, models.DO_NOTHING, db_column='sysmapid')
    elementid = models.BigIntegerField()
    elementtype = models.IntegerField()
    iconid_off = models.ForeignKey(Images, models.DO_NOTHING, db_column='iconid_off', blank=True, null=True, related_name="sysmap_icon_off")
    iconid_on = models.ForeignKey(Images, models.DO_NOTHING, db_column='iconid_on', blank=True, null=True, related_name="sysmap_icon_on")
    label = models.CharField(max_length=2048)
    label_location = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    iconid_disabled = models.ForeignKey(Images, models.DO_NOTHING, db_column='iconid_disabled', blank=True, null=True, related_name="sysmap_disabled_icon")
    iconid_maintenance = models.ForeignKey(Images, models.DO_NOTHING, db_column='iconid_maintenance', blank=True, null=True, related_name="sysmap_maintenance_icon")
    elementsubtype = models.IntegerField()
    areatype = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    viewtype = models.IntegerField()
    use_iconmap = models.IntegerField()
    application = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sysmaps_elements'


class SysmapsLinkTriggers(models.Model):
    linktriggerid = models.BigIntegerField(primary_key=True)
    linkid = models.ForeignKey('SysmapsLinks', models.DO_NOTHING, db_column='linkid')
    triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid')
    drawtype = models.IntegerField()
    color = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'sysmaps_link_triggers'
        unique_together = (('linkid', 'triggerid'),)


class SysmapsLinks(models.Model):
    linkid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey(Sysmaps, models.DO_NOTHING, db_column='sysmapid')
    selementid1 = models.ForeignKey(SysmapsElements, models.DO_NOTHING, db_column='selementid1', related_name="sysmapslink_selementid1")
    selementid2 = models.ForeignKey(SysmapsElements, models.DO_NOTHING, db_column='selementid2', related_name="sysmapslink_selementid2")
    drawtype = models.IntegerField()
    color = models.CharField(max_length=6)
    label = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'sysmaps_links'


class Task(models.Model):
    taskid = models.BigIntegerField(primary_key=True)
    type = models.IntegerField()
    status = models.IntegerField()
    clock = models.IntegerField()
    ttl = models.IntegerField()
    proxy_hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='proxy_hostid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class TaskAcknowledge(models.Model):
    taskid = models.OneToOneField(Task, models.DO_NOTHING, db_column='taskid', primary_key=True)
    acknowledgeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'task_acknowledge'


class TaskCloseProblem(models.Model):
    taskid = models.OneToOneField(Task, models.DO_NOTHING, db_column='taskid', primary_key=True)
    acknowledgeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'task_close_problem'


class TaskRemoteCommand(models.Model):
    taskid = models.OneToOneField(Task, models.DO_NOTHING, db_column='taskid', primary_key=True)
    command_type = models.IntegerField()
    execute_on = models.IntegerField()
    port = models.IntegerField()
    authtype = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    publickey = models.CharField(max_length=64)
    privatekey = models.CharField(max_length=64)
    command = models.TextField()
    alertid = models.BigIntegerField(blank=True, null=True)
    parent_taskid = models.BigIntegerField()
    hostid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'task_remote_command'


class TaskRemoteCommandResult(models.Model):
    taskid = models.OneToOneField(Task, models.DO_NOTHING, db_column='taskid', primary_key=True)
    status = models.IntegerField()
    parent_taskid = models.BigIntegerField()
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'task_remote_command_result'


class Timeperiods(models.Model):
    timeperiodid = models.BigIntegerField(primary_key=True)
    timeperiod_type = models.IntegerField()
    every = models.IntegerField()
    month = models.IntegerField()
    dayofweek = models.IntegerField()
    day = models.IntegerField()
    start_time = models.IntegerField()
    period = models.IntegerField()
    start_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timeperiods'


class Trends(models.Model):
    itemid = models.BigIntegerField(primary_key=True)
    clock = models.IntegerField()
    num = models.IntegerField()
    value_min = models.FloatField()
    value_avg = models.FloatField()
    value_max = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trends'
        unique_together = (('itemid', 'clock'),)


class TrendsUint(models.Model):
    itemid = models.BigIntegerField(primary_key=True)
    clock = models.IntegerField()
    num = models.IntegerField()
    value_min = models.BigIntegerField()
    value_avg = models.BigIntegerField()
    value_max = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'trends_uint'
        unique_together = (('itemid', 'clock'),)


class TriggerDepends(models.Model):
    triggerdepid = models.BigIntegerField(primary_key=True)
    triggerid_down = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid_down', related_name="depend_trigger_down")
    triggerid_up = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid_up', related_name="depend_trigger_up")

    class Meta:
        managed = False
        db_table = 'trigger_depends'
        unique_together = (('triggerid_down', 'triggerid_up'),)


class TriggerDiscovery(models.Model):
    triggerid = models.OneToOneField('Triggers', models.DO_NOTHING, db_column='triggerid', primary_key=True, related_name="discovery_trigger")
    parent_triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='parent_triggerid', related_name="discovery_parent_trigger")

    class Meta:
        managed = False
        db_table = 'trigger_discovery'


class TriggerTag(models.Model):
    triggertagid = models.BigIntegerField(primary_key=True)
    triggerid = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggerid')
    tag = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'trigger_tag'


class Triggers(models.Model):
    triggerid = models.BigIntegerField(primary_key=True)
    expression = models.CharField(max_length=2048)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    status = models.IntegerField()
    value = models.IntegerField()
    priority = models.IntegerField()
    lastchange = models.IntegerField()
    comments = models.TextField()
    error = models.CharField(max_length=2048)
    templateid = models.ForeignKey('self', models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    type = models.IntegerField()
    state = models.IntegerField()
    flags = models.IntegerField()
    recovery_mode = models.IntegerField()
    recovery_expression = models.CharField(max_length=2048)
    correlation_mode = models.IntegerField()
    correlation_tag = models.CharField(max_length=255)
    manual_close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'triggers'


class Users(models.Model):
    userid = models.BigIntegerField(primary_key=True)
    alias = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
    autologin = models.IntegerField()
    autologout = models.CharField(max_length=32)
    lang = models.CharField(max_length=5)
    refresh = models.CharField(max_length=32)
    type = models.IntegerField()
    theme = models.CharField(max_length=128)
    attempt_failed = models.IntegerField()
    attempt_ip = models.CharField(max_length=39)
    attempt_clock = models.IntegerField()
    rows_per_page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usrgrpid = models.ForeignKey('Usrgrp', models.DO_NOTHING, db_column='usrgrpid')
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('usrgrpid', 'userid'),)


class Usrgrp(models.Model):
    usrgrpid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    gui_access = models.IntegerField()
    users_status = models.IntegerField()
    debug_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usrgrp'


class Valuemaps(models.Model):
    valuemapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'valuemaps'


class Widget(models.Model):
    widgetid = models.BigIntegerField(primary_key=True)
    dashboardid = models.ForeignKey(Dashboard, models.DO_NOTHING, db_column='dashboardid')
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'widget'


class WidgetField(models.Model):
    widget_fieldid = models.BigIntegerField(primary_key=True)
    widgetid = models.ForeignKey(Widget, models.DO_NOTHING, db_column='widgetid')
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    value_int = models.IntegerField()
    value_str = models.CharField(max_length=255)
    value_groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='value_groupid', blank=True, null=True)
    value_hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='value_hostid', blank=True, null=True)
    value_itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='value_itemid', blank=True, null=True)
    value_graphid = models.ForeignKey(Graphs, models.DO_NOTHING, db_column='value_graphid', blank=True, null=True)
    value_sysmapid = models.ForeignKey(Sysmaps, models.DO_NOTHING, db_column='value_sysmapid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget_field'
