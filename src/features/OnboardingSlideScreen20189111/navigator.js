import { createStackNavigator } from "react-navigation-stack";

import Onboarding from "./screens/";

export default OnboardingBlueprintNavigator = createStackNavigator(
  {
    Onboarding: { screen: Onboarding }
  },
  {
    initialRouteName: "Onboarding",
    defaultNavigationOptions: ({ navigation }) => ({ header: null }),
  }
);
