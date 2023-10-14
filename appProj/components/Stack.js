import * as React from "react";
import { View, Text } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Home from "./home";
import Create from "./Create";
import Edit from "./Edit";

const Stack = createNativeStackNavigator();

function Navigator() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Home" component={Home} />
      <Stack.Screen name="Edit" component={Edit} />
      <Stack.Screen name="Create" component={Create} />
    </Stack.Navigator>
  );
}

export default Navigator;
