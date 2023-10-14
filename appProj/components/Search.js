import * as React from "react";
import { Searchbar } from "react-native-paper";

const Search = (props) => {



   
  return (
    <Searchbar
      placeholder="Search"
      onChangeText={(text) => props.setSearchQuery(text)}
      value={props.searchQuery}
    />
  );
};

export default Search;
