import React, { useState ,useEffect} from 'react'
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';

function Create(props) {
  const [data,setData]=useState("")
  const [accept, setAccept] = useState("False");


const readData = () => {
  fetch('http://127.0.0.1:8080/create', {
    method: "GET",
    cors:"no-cors",
  })
    .then((resp) => resp.json()
   )
    .then((info) => setData(info.results))
    .catch((error) => console.log(error));
};

const postData = () => {
  fetch(`http://127.0.0.1:8080/create`, {
    method: "POST",
    cors: "no-cors",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ accept: accept }),
  })
    .then((resp) => resp.json())
    .then((info) => {
      setData(info.results);
    
      setAccept("False")
    })
    .catch((error) => console.log(error));
};


useEffect(postData,[,accept]);
useEffect(readData);
console.log(accept);
  return (
    <Button
      icon="download"
      mode="contained"
      onPress={() => (setAccept("True"), window.location.reload())}
    >
      {data}
    </Button>
  );
}

export default Create
