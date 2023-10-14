import React, { useState } from "react";
import { View , Text} from "react-native";
import { TextInput,Button, styles } from "react-native-paper";

function Edit(props) {
  const data = props.route.params.item;

  const [hospital, setHospital] = useState(data.Hospital);
  const [device, setDevice] = useState(data.Device);

const updateData=()=> {
   fetch(`http://127.0.0.1:8080/edit/${data.id}/`, {
     method: 'PUT',
     headers: { 'Content-Type': 'application/json'},
     body: JSON.stringify({ hospital: hospital, device: device })
   })
     .then((resp) => resp.json())
     .then((data) => {
       props.navigation.navigate('Home',{data:data});
       window.location.reload();

      
     })
     .catch((error) => console.log(error));




}

  return (
    <View>
      <TextInput
        label="Hospital Name"
        value={hospital}
        mode="outlined"
        onChangeText={(text) => setHospital(text)}
      />
      <TextInput
        label="Device Number"
        value={device}
        mode="outlined"
        onChangeText={(text) => setDevice(text)}
      />
      <Button
      icon='update'
      mode='contained'
      onPress={()=>updateData()}>
        update article

      </Button>
    </View>
  );
}

export default Edit;
