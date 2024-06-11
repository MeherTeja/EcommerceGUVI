import boto3
import uuid
import json
import datetime
from environments import secret_keys_1
aws_access_key_id=secret_keys_1.aws_access_key_id
aws_secret_access_key=secret_keys_1.aws_secret_access_key
aws_region='ap-south-1'
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)
def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 

for i in range(3):
    truck_id=input("Enter truck id")
    print("Enter gps location")
    latitude=float(input("Enter latitude"))
    long=float(input("Enter longitude"))
    altitude=float(input("Enter altitude"))  
    speed=float(input("Enter speed"))
    vehicle_speed=float(input("Enter vehicle speed"))
    print("Enter engine diagnos")
    engine_rpm=int(input("Enter engine_rpm"))
    fuel_level=float(input("Enter fuel level"))
    temp=float(input("Enter temperature"))
    oil_press=float(input("Enter oil pressure"))
    battery_voltage=float(input("Enter battery voltage"))
    odometer_reading=float(input("Enter odometer reading"))
    fuel_cons=float(input("Enter fuel consumption"))
    print('Vehicle health and maintainence..')
    brake_status=input("Enter brake status")
    print("Tire pressure")
    front_left=float(input("Enter float_left"))
    front_right=float(input("Enter float_right"))
    rear_left=float(input("Enter rear_left"))
    rear_right=float(input("Enter rear_right"))
    transmission=input("Enter transmission")
    print("Environmental conditions")
    temp1=float(input("Enter temp1"))
    humidity=float(input("Enter humidity"))
    atmospheric_pressure=float(input("Enter atmos_pressure"))
    dt=datetime.datetime.now()
    json_dt=json.dumps(dt, default=serialize_datetime) 
    post_data={
        'truck_id':truck_id,
        'latitude':latitude,
        'longitude':long,
        'altitude':altitude,
        'speed':speed,
        'vehicle_speed':vehicle_speed,
        'engine_rpm':engine_rpm,
        'fuel_level':fuel_level,
        'temp':temp,
        'oil_pressure':oil_press,
        'battery_voltage':battery_voltage,
        'odometer_reading':odometer_reading,
        'fuel_consumption':fuel_cons,
        'brake_status':brake_status,
        'front_left':front_left,
        'front_right':front_right,
        'rear-left':rear_left,
        'rear_right':rear_right,
        'transmission':transmission,
        'temp1':temp1,
        'humidity':humidity,
        'atmospheric_pressure':atmospheric_pressure,
        'timestamp':json_dt
    }
    var1=json.dumps(post_data)
    response=lambda_client.invoke(
        FunctionName='lambda_api_data_1',
        Payload=var1
    )
print(response)
