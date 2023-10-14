import * as React from 'react'
import {View,Text,FlatList} from 'react-native';
import { DataTable, Searchbar } from "react-native-paper";
import Search from "./Search";
const numberOfItemsPerPageList = [2, 3, 4,6,8,10];

function Home(props) {

const [item,setRead] = React.useState([{}])
  const [searchQuery, setSearchQuery] = React.useState("");
  const onChangeSearch = (query) => setSearchQuery(query);

const postData = () => {
  fetch(`http://127.0.0.1:8080/read`, {
    method: "POST",
    cors: "no-cors",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ "serial": searchQuery }),
  })
    .then((resp) => resp.json())
    .then((item) => setRead(item))
    .catch((error) => console.log(error));
};
 React.useEffect(postData, [searchQuery]);



  const [page, setPage] = React.useState(0);
  const [numberOfItemsPerPage, onItemsPerPageChange] = React.useState(numberOfItemsPerPageList[numberOfItemsPerPageList.length - 1]);
  const from = page * numberOfItemsPerPage;
  const to = Math.min((page + 1) * numberOfItemsPerPage, item.length);


  function changenumber (){
    onItemsPerPageChange(numberOfItemsPerPage + 4)
  }
  React.useEffect(() => {
     setPage(0);
  }, [numberOfItemsPerPage]);




return (
  <DataTable>
    <Searchbar
      placeholder="Search"
      onChangeText={(text) => setSearchQuery(text)}
      value={searchQuery}
    />
    <DataTable.Header>
      <DataTable.Title>Hospital</DataTable.Title>
      <DataTable.Title>Device</DataTable.Title>
      <DataTable.Title>SN</DataTable.Title>
      <DataTable.Title>MAC</DataTable.Title>
      <DataTable.Title>DateAdded</DataTable.Title>
    </DataTable.Header>

    {item.slice(from, to).map((item) => (
      <DataTable.Row
        key={item.key}
        onPress={() => props.navigation.navigate("Edit", { item })}
      >
        <DataTable.Cell>{item.Hospital}</DataTable.Cell>
        <DataTable.Cell>{item.Device}</DataTable.Cell>
        <DataTable.Cell>{item.SN}</DataTable.Cell>
        <DataTable.Cell>{item.MAC}</DataTable.Cell>
        <DataTable.Cell>{item.DateAdded}</DataTable.Cell>
      </DataTable.Row>
    ))}
    <DataTable.Pagination
      page={page}
      numberOfPages={Math.ceil(item.length / numberOfItemsPerPage)}
      onPageChange={(page) => setPage(page)}
      label={`${from + 1}-${to} of ${item.length}`}
      showFastPaginationControls
      numberOfItemsPerPageList={numberOfItemsPerPageList}
      numberOfItemsPerPage={numberOfItemsPerPage}
      onItemsPerPageChange={onItemsPerPageChange}
      selectPageDropdownLabel={"Rows per page"}
    />
  </DataTable>
);
};

export default Home
