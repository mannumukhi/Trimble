import json
alert_data = '{"header":{"packet_info":"valid","packet_type":"RT","vehicle_type":"EDC","packet_seq":"1",' \
            '"checksum":"10"}, "message_type":"EMR","IMEI":"012345678901234","packet_type":"NM",' \
            '"date_time":"220714050656","gps_val":"A","latitude":28.758963,"lat_dir":"N",' \
            '"longitude":77.6277844,"long_dir":"W","Altitude":183.5,"speed":25.1f,' \
            '"direction":23.4567f,"gps_provider":"G","veh_reg_no":"DL1PC9821",' \
             '"reply_num":"9849058167","checksum":"10"}'

alert_json = json.loads(alert_data)
"""
def header():
    global y
"""

# ****************** Message type Testcaes ************************* #
def msg_presence():
    global alert_json
    if "message_type" in alert_json:
        return 1

def msg_type():
    global alert_json
    if "message_type" in alert_json:
        return alert_json["message_type"]

def msg_data_type():
    global alert_json
    if "message_type" in alert_json:
        return type(alert_json["message_type"])

def msg_size():
    global alert_json
    if "message_type" in alert_json:
        return len(alert_json["message_type"])

# ****************** IMEI Testcaes ************************* #
def imei_presence():
    global alert_json
    if "IMEI" in alert_json:
        return 1

def imei_size():
    global alert_json
    if "IMEI" in alert_json:
        return len(alert_json["IMEI"])

def imei_data_type():
    global alert_json
    if "IMEI" in alert_json:
        return type(alert_json["IMEI"])

# ****************** Packet type Testcaes ************************* #
def pckt_presence():
    global alert_json
    if "packet_type" in alert_json:
        return 1

def pckt_size():
    global alert_json
    if "packet_type" in alert_json:
        return len(alert_json["packet_type"])

def pckt_data_type():
    global alert_json
    if "packet_type" in alert_json:
        return type(alert_json["packet_type"])

def pckt_type():
    global alert_json
    if "packet_type" in alert_json:
        return alert_json["packet_type"]

# ****************** Date & Time Testcaes ************************* #
def date_time_presence():
    global alert_json
    if "date_time" in alert_json:
        return 1

def date_time_size():
    global alert_json
    if "date_time" in alert_json:
        return len(alert_json["date_time"])

def date_time_data_type():
    global alert_json
    if "date_time" in alert_json:
        return type(alert_json["date_time"])

# ****************** GPS validity Testcaes ************************* #
def gps_validity_presence():
    global alert_json
    if "gps_val" in alert_json:
        return 1

def gps_validity_size():
    global alert_json
    if "gps_val" in alert_json:
        return len(alert_json["gps_val"])

def gps_validity_data_type():
    global alert_json
    if "gps_val" in alert_json:
        return type(alert_json["gps_val"])

def gps_validity_type():
    global alert_json
    if "gps_val" in alert_json:
        return alert_json["gps_val"]

# ****************** Latitude Testcaes ************************* #
def latitude_presence():
    global alert_json
    if "latitude" in alert_json:
        return 1

def latitude_size():
    global alert_json
    if "latitude" in alert_json:
        return len(alert_json["latitude"])

def latitude_data_type():
    global alert_json
    if "latitude" in alert_json:
        return type(alert_json["latitude"])

# ****************** Latitude_Direction Testcaes ************************* #
def lat_dir_presence():
    global alert_json
    if "lat_dir" in alert_json:
        return 1

def lat_dir_size():
    global alert_json
    if "lat_dir" in alert_json:
        return len(alert_json["lat_dir"])

def lat_dir_data_type():
    global alert_json
    if "lat_dir" in alert_json:
        return type(alert_json["lat_dir"])

def lat_dir_type():
    global alert_json
    if "lat_dir" in alert_json:
        return alert_json["lat_dir"]

# ****************** Longitude Testcaes ************************* #
def longitude_presence():
    global alert_json
    if "longitude" in alert_json:
        return 1

def longitude_size():
    global alert_json
    if "longitude" in alert_json:
        return len(alert_json["longitude"])

def longitude_data_type():
    global alert_json
    if "longitude" in alert_json:
        return type(alert_json["longitude"])

# ****************** Latitude_Direction Testcaes ************************* #
def long_dir_presence():
    global alert_json
    if "long_dir" in alert_json:
        return 1

def long_dir_size():
    global alert_json
    if "long_dir" in alert_json:
        return len(alert_json["long_dir"])

def long_dir_data_type():
    global alert_json
    if "long_dir" in alert_json:
        return type(alert_json["long_dir"])

def long_dir_type():
    global alert_json
    if "long_dir" in alert_json:
        return alert_json["long_dir"]

# ****************** Altitude Testcaes ************************* #
def altitude_presence():
    global alert_json
    if "Altitude" in alert_json:
        return 1

def altitude_size():
    global alert_json
    if "Altitude" in alert_json:
        return len(alert_json["Altitude"])

def altitude_data_type():
    global alert_json
    if "Altitude" in alert_json:
        return type(alert_json["Altitude"])

# ****************** Speed Testcaes ************************* #
def speed_presence():
    global alert_json
    if "speed" in alert_json:
        return 1

def speed_size():
    global alert_json
    if "speed" in alert_json:
        return len(alert_json["speed"])

def speed_data_type():
    global alert_json
    if "speed" in alert_json:
        return type(alert_json["speed"])

# ****************** Direction Testcaes ************************* #
def direction_presence():
    global alert_json
    if "direction" in alert_json:
        return 1

def direction_size():
    global alert_json
    if "direction" in alert_json:
        return len(alert_json["direction"])

def direction_data_type():
    global alert_json
    if "direction" in alert_json:
        return type(alert_json["direction"])

# ****************** GPS Provider Testcaes ************************* #
def gps_provider_presence():
    global alert_json
    if "gps_provider" in alert_json:
        return 1

def gps_provider_size():
    global alert_json
    if "gps_provider" in alert_json:
        return len(alert_json["gps_provider"])

def gps_provider_data_type():
    global alert_json
    if "gps_provider" in alert_json:
        return type(alert_json["gps_provider"])

def gps_provider_type():
    global alert_json
    if "gps_provider" in alert_json:
        return alert_json["gps_provider"]

# ****************** Vehicle Registration Number Testcaes ************************* #
def vehicle_reg_num_presence():
    global alert_json
    if "veh_reg_no" in alert_json:
        return 1

def vehicle_reg_num_size():
    global alert_json
    if "veh_reg_no" in alert_json:
        return len(alert_json["veh_reg_no"])

def vehicle_reg_num_data_type():
    global alert_json
    if "veh_reg_no" in alert_json:
        return type(alert_json["veh_reg_no"])

# ****************** Reply Number Testcaes ************************* #
def reply_num_presence():
    global alert_json
    if "reply_num" in alert_json:
        return 1

def reply_num_size():
    global alert_json
    if "reply_num" in alert_json:
        return len(alert_json["reply_num"])

# ****************** Check-sum Testcaes ************************* #
def checkSum_presence():
    global alert_json
    if "checksum" in alert_json:
        return 1

def checkSum_size():
    global alert_json
    if "checksum" in alert_json:
        return len(alert_json["checksum"])


