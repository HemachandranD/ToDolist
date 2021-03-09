#!/usr/bin/env python
from flask import Flask, jsonify, request
import json
from flask_restful import Resource, Api
import os


self_heal = []

Tomcat_nodes = [
    "ahlt1056.ah.nl",
    "ahla1065.ah.nl",
    "ahla1067.ah.nl",
    "ahlp1078.ah.nl",
    "ahlp1079.ah.nl",
    "ahlp1080.ah.nl",
    "ahlp1589.ah.nl",
    "ahlp1590.ah.nl",
]
FR_nodes = [
    "ahlt1020.ah.nl",
    "ahla1016.ah.nl",
    "ahla1017.ah.nl",
    "ahlp1021.ah.nl",
    "ahlp1022.ah.nl",
    "ahlp1023.ah.nl",
    "ahlp1024.ah.nl",
]


hostservice_map = [
    "ahlt1056.ah.nlTomcat",
    "ahla1065.ah.nlTomcat",
    "ahla1067.ah.nlTomcat",
    "ahlp1078.ah.nlTomcat",
    "ahlp1079.ah.nlTomcat",
    "ahlp1080.ah.nlTomcat",
    "ahlp1589.ah.nlTomcat",
    "ahlp1590.ah.nlTomcat",
    "ahlt1056.ah.nlApache",
    "ahla1065.ah.nlApache",
    "ahla1067.ah.nlApache",
    "ahlp1078.ah.nlApache",
    "ahlp1079.ah.nlApache",
    "ahlp1080.ah.nlApache",
    "ahlp1589.ah.nlApache",
    "ahlp1590.ah.nlApache",
    "alhmsvlaapp0008Tomcat",
    "alhmsvlaapp0009Tomcat",
    "alhmsvlpapp0008Tomcat",
    "alhmsvlpapp0009Tomcat",
    "alhmsvlaapp0006Tomcat",
    "alhmsvlaapp0007Tomcat",
    "alhmsvlpapp0004Tomcat",
    "alhmsvlpapp0005Tomcat",
    "alhmsvlaapp0008Apache",
    "alhmsvlaapp0009Apache",
    "alhmsvlpapp0008Apache",
    "alhmsvlpapp0009Apache",
    "alhmsvlaapp0006Apache",
    "alhmsvlaapp0007Apache",
    "alhmsvlpapp0004Apache",
    "alhmsvlpapp0005Apache",
    "ahlt1027.ah.nlAdmin",
    "ahlt1028.ah.nlAdmin",
    "ahla1057.ah.nlAdmin",
    "ahla1059.ah.nlAdmin",
    "ahla1060.ah.nlAdmin",
    "ahlp1074.ah.nlAdmin",
    "ahlp1075.ah.nlAdmin",
    "ahlt1027.ah.nlRos",
    "ahlt1028.ah.nlRos",
    "ahla1057.ah.nlRos",
    "ahla1059.ah.nlRos",
    "ahla1060.ah.nlRos",
    "ahlp1074.ah.nlRos",
    "ahlp1075.ah.nlRos",
    "ahlt1020.ah.nlAdmin",
    "ahla1016.ah.nlAdmin",
    "ahla1017.ah.nlAdmin",
    "ahlp1021.ah.nlAdmin",
    "ahlp1022.ah.nlAdmin",
    "ahlp1023.ah.nlAdmin",
    "ahlp1024.ah.nlAdmin",
    "ahlt1020.ah.nlProm",
    "ahla1016.ah.nlProm",
    "ahla1017.ah.nlProm",
    "ahlp1021.ah.nlProm",
    "ahlp1022.ah.nlProm",
    "ahlp1023.ah.nlProm",
    "ahlp1024.ah.nlProm",
    "ahlt1020.ah.nlRset",
    "ahla1016.ah.nlRset",
    "ahla1017.ah.nlRset",
    "ahlp1021.ah.nlRset",
    "ahlp1022.ah.nlRset",
    "ahlp1023.ah.nlRset",
    "ahlp1024.ah.nlRset",
    "ahlt1020.ah.nlForms",
    "ahla1016.ah.nlForms",
    "ahla1017.ah.nlForms",
    "ahlp1021.ah.nlForms",
    "ahlp1022.ah.nlForms",
    "ahlp1023.ah.nlForms",
    "ahlp1024.ah.nlForms",
    "ahlt1020.ah.nlReports",
    "ahla1016.ah.nlReports",
    "ahla1017.ah.nlReports",
    "ahlp1021.ah.nlReports",
    "ahlp1022.ah.nlReports",
    "ahlp1023.ah.nlReports",
    "ahlp1024.ah.nlReports",
    "ahlt1414.ah.nlAdmin",
    "ahlt1421.ah.nlAdmin",
    "ahla1526.ah.nlAdmin",
    "ahlp1528.ah.nlAdmin",
    "ahlp1530.ah.nlAdmin",
    "ahla1526.ah.nlFtlc",
    "ahla1527.ah.nlFtlc",
    "ahlp1528.ah.nlFtlc",
    "ahlp1529.ah.nlFtlc",
    "ahlp1530.ah.nlFtlc",
    "ahlp1531.ah.nlFtlc",
    "ahlt1414.ah.nlIvil",
    "ahlt1421.ah.nlIvil",
    "ahla1526.ah.nlIvil",
    "ahla1527.ah.nlIvil",
    "ahlp1528.ah.nlIvil",
    "ahlp1529.ah.nlIvil",
    "ahlp1530.ah.nlIvil",
    "ahlp1531.ah.nlIvil",
    "ahlt1414.ah.nlMdcz",
    "ahlt1421.ah.nlMdcz",
    "ahla1526.ah.nlMdcz",
    "ahla1527.ah.nlMdcz",
    "ahlt1414.ah.nlQtro",
    "ahlt1421.ah.nlQtro",
    "ahla1526.ah.nlQtro",
    "ahla1527.ah.nlQtro",
    "ahlp1528.ah.nlQtro",
    "ahlp1529.ah.nlQtro",
    "ahlp1530.ah.nlQtro",
    "ahlp1531.ah.nlQtro",
    "ahlt1414.ah.nlVera",
    "ahla1526.ah.nlVera",
    "ahla1527.ah.nlVera",
    "ahlp1528.ah.nlVera",
    "ahlp1529.ah.nlVera",
    "ahlp1530.ah.nlVera",
    "ahlp1531.ah.nlVera",
    "ahla1018.ah.nlIhs",
    "ahla1019.ah.nlIhs",
    "ahlp1025.ah.nlIhs",
    "ahlp1026.ah.nlIhs",
    "ahla1712.ah.nlIhs",
    "ahla1713.ah.nlIhs",
    "ahlp1710.ah.nlIhs",
    "ahlp1711.ah.nlIhs",
    "ahx027.ahold.euIhs",
    "ahx029.ahold.euIhs",
    "ahx030.ahold.euIhs",
    "ahx032.ahold.euIhs",
    "ahx021.ahold.euIhs",
    "ahx024.ahold.euIhs",
    "ahx037.ahold.euIhs",
    "ahx040.ahold.euIhs",
    "ahla1712.ah.nlDcre",
    "ahla1713.ah.nlDcre",
    "ahlp1710.ah.nlDcre",
    "ahlp1711.ah.nlDcre",
    "ahx031.ahold.euWfm",
    "ahx033.ahold.euWfm",
    "ahx035.ahold.euWfm" "ahx034.ahold.euWfm",
    "ahx036.ahold.euWfm",
    "ahx038.ahold.euWfm",
    "ahla2192.ah.nlApache",
    "ahlp2194.ah.nlApache",
    "ahla1512.ah.nlApache",
    "ahlp1514.ah.nlApache",
    "ahlp2016.ah.nlApache",
    "ahlp2017.ah.nlApache",
    "ahlp2026.ah.nlApache",
    "ahlp2027.ah.nlApache",
    "ahlp1099.ah.nlApache",
    "ahlp1100.ah.nlApache",
    "ahx021.ahold.euCognos",
    "ahx024.ahold.euCognos",
    "ahx037.ahold.euCognos",
    "ahx040.ahold.euCognos",
]

imap = {
    "ahlt1056.ah.nl": "samtst",
    "ahla1065.ah.nl": "samacc01",
    "ahla1067.ah.nl": "samacc02",
    "ahlp1078.ah.nl": "samprd01",
    "ahlp1079.ah.nl": "samprd02",
    "ahlp1080.ah.nl": "samprd03",
    "ahlp1589.ah.nl": "samprd04",
    "ahlp1590.ah.nl": "samprd05",
    "alhmsvlaapp0006": "acceber01",
    "alhmsvlaapp0007": "acceber02",
    "alhmsvlpapp0004": "prdeber01",
    "alhmsvlpapp0005": "prdeber02",
    "alhmsvlaapp0008": "accdedi01",
    "alhmsvlaapp0009": "accdedi02",
    "alhmsvlpapp0008": "prddedi01",
    "alhmsvlpapp0009": "prddedi02",
    "ahlt1020.ah.nl": "tst_FR",
    "ahla1016.ah.nl": "acc_FR01",
    "ahla1017.ah.nl": "acc_FR02",
    "ahlp1021.ah.nl": "prd_FR01",
    "ahlp1022.ah.nl": "prd_FR02",
    "ahlp1023.ah.nl": "prd_FR03",
    "ahlp1024.ah.nl": "prd_FR04",
    "ahlt1027.ah.nl": "sit_ros",
    "ahlt1028.ah.nl": "rostst",
    "ahla1057.ah.nl": "bfx_ros",
    "ahla1059.ah.nl": "uat_ros01",
    "ahla1060.ah.nl": "uat_ros02",
    "ahlp1074.ah.nl": "prd_ros01",
    "ahlp1075.ah.nl": "prd_ros02",
    "ahla1712.ah.nl": "dcreacc01",
    "ahla1713.ah.nl": "dcreacc02",
    "ahlp1710.ah.nl": "dcreprd01",
    "ahlp1711.ah.nl": "dcreprd02",
    "ahx027.ahold.eu": "wfmaccihs01",
    "ahx029.ahold.eu": "wfmaccihs02",
    "ahx031.ahold.eu": "wfmacc01",
    "ahx033.ahold.eu": "wfmacc02",
    "ahx035.ahold.eu": "wfmacc03",
    "ahx030.ahold.eu": "wfmprdihs01",
    "ahx032.ahold.eu": "wfmprdihs02",
    "ahx034.ahold.eu": "wfmprd01",
    "ahx036.ahold.eu": "wfmprd02",
    "ahx038.ahold.eu": "wfmprd03",
    "ahla2192.ah.nl": "dagacc",
    "ahlp2194.ah.nl": "dagprd",
    "ahla1512.ah.nl": "emosacchttpd",
    "ahlp1514.ah.nl": "emosprdhttpd",
    "ahlp2016.ah.nl": "ecmprd01",
    "ahlp2017.ah.nl": "ecmprd02",
    "ahlp2026.ah.nl": "ecmprd03",
    "ahlp2027.ah.nl": "ecmprd04",
    "ahlp1099.ah.nl": "vtrbprd",
    "ahlp1100.ah.nl": "mscbprd",
    "ahx021.ahold.eu": "sitcgns",
    "ahx024.ahold.eu": "bfxcgns",
    "ahx037.ahold.eu": "uatcgns",
    "ahx040.ahold.eu": "prdcgns",
}

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return "Hello Team, Welcome to Self Heal!"


class NodeService(Resource):
    def get(self):
        parameters = request.args
        self_heal.append(parameters)
        self.extract_params()
        self.check()
        return jsonify(self_heal)

    def extract_params(self):
        for lists in self_heal:
            self.Node = lists["node"]
            self.Service = lists["service"]
            print(self.Node)
            print(self.Service)
            self.ns = self.Node + self.Service.capitalize()
            print(self.ns)

    def check(self):
        if self.ns in hostservice_map:
            self.group = imap[self.Node]
            print(self.group)
            self.nsmatch()
        else:
            print("Host & service doesn't exist")

    def nsmatch(self):
        if self.Node in Tomcat_nodes and self.Service == "Tomcat":
            os.system(
                'make run playbook=tomcat args="-e variable_host=' + self.group + '"'
            )

    # def playbookrun(self, playbook_path):
    #     hosts_path = "/Self_Heal/hosts.ini"
    #     stats = callbacks.AggregateStats()
    #     playbook_cb = callbacks.PlaybookCallbacks(verbose=0)
    #     runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=0)
    #     playbook.PlayBook(
    #         playbook=playbook_path,
    #         host_list=hosts_path,
    #         stats=stats,
    #         callbacks=playbook_cb,
    #         runner_callbacks=runner_cb,
    #     ).run()
    #     return stats


api.add_resource(NodeService, "/selfheal")
api.add_resource(Home, "/")
app.run(port=5000)
