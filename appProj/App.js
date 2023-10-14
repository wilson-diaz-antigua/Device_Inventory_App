
import { MD3LightTheme as DefaultTheme, AppRegistry } from "react-native";
import { Provider as PaperProvider,Button} from "react-native-paper";


import { NavigationContainer } from "@react-navigation/native";
import Navigator from "./components/Stack";
import Create from "./components/Create";
const theme = {
  ...DefaultTheme,
};

export default function App() {
  return (
    <PaperProvider theme={theme}>
      <NavigationContainer>
        <Navigator />

      <Create/>
      </NavigationContainer>

    </PaperProvider>
  );
}
