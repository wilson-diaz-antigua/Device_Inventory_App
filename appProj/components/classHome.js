import React, { Component } from 'react';
import {View,Text} from 'react-native';


 class ClassHome extends Component {

    state ={
        name:"name dummy"
    }
  render() {
    return (
      <View>
        <Text>class home {this.state.name}</Text>
       
      </View>
    )
  }
}

export default ClassHome
