import { MD3LightTheme as DefaultTheme } from "react-native";
import { Provider as PaperProvider } from "react-native-paper";

import { NavigationContainer } from "@react-navigation/native";
import Create from "./components/Create";
import Navigator from "./components/Stack";
const theme = {
  ...DefaultTheme,
};

export default function App() {
  return (
    <PaperProvider theme={theme}>
      <NavigationContainer>
        <Navigator />

        <Create />
      </NavigationContainer>
    </PaperProvider>
  );
}

import React from "react";
