import streamlit as st
import boto3
import uuid
import json
from environments import secret_keys
aws_access_key_id=secret_keys.aws_access_key_id
aws_secret_access_key=secret_keys.aws_secret_access_key
aws_region='ap-south-1'
    
#Integrating with aws kinesis
kinesis_client = boto3.client(
    'kinesis',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

stream_name="firstkinesis"
st.title('Items page')
col1,col2,col3=st.columns(3)


with col1:
    item_name_1="Mobile"
    st.header(item_name_1)
    item_id_1=1
    st.write("Item id :",item_id_1)
    st.image("C://Users//Meher Teja//Pictures//mobile.png",width=50)
    if 'count' not in st.session_state:
        st.session_state.count=0
    it1=st.button('choose mobile')
    if it1:
         st.session_state.count+=1
    st.write('Click cnt=',st.session_state.count)
    
    post_data={
        'item_id':item_id_1,
        'item_name':item_name_1,
        'click_cnt':st.session_state.count
    }
    
    var1=json.dumps(post_data)
    response=kinesis_client.put_record(StreamName=stream_name,Data=var1,PartitionKey='item_id_1')
    print(response)

with col2:
    item_name_2="Laptop"
    item_id_2=2
    st.write("Item id :",item_id_2)
    st.image("C://Users//Meher Teja//Pictures//laptop.jpg",width=100)
    if 'count1' not in st.session_state:
        st.session_state.count1=0
    it2=st.button('choose lappy')
    if it2:
         st.session_state.count1+=1
    st.write('Click cnt=',st.session_state.count1)

    post_data_1={
        'item_id':item_id_2,
        'item_name':item_name_2,
        'click_cnt':st.session_state.count1
    }

    var2=json.dumps(post_data_1)
    response=kinesis_client.put_record(StreamName=stream_name,Data=var2,PartitionKey='item_id_2')
    print(response)

with col3:
    item_name_3="Smartwatch"
    item_id_3=10
    st.write("Item id :",item_id_3)
    st.image("C://Users//Meher Teja//Pictures//smartwatch.jpg",width=50)
    if 'count2' not in st.session_state:
        st.session_state.count2=0
    it3=st.button('choose smartwatch')
    if it3:
         st.session_state.count2+=1
    st.write('Click cnt=',st.session_state.count2)

    post_data_3={
        'item_id':item_id_3,
        'item_name':item_name_3,
        'click_cnt':st.session_state.count2
    }

    var3=json.dumps(post_data_3)
    response=kinesis_client.put_record(StreamName=stream_name,Data=var3,PartitionKey='item_id_3')
    print(response)