import React, { Component } from 'react';
import '../styles/App.css';
import FacebookLogin from 'react-facebook-login';

const responseFacebook = (response) => {
  console.log(response)
}


class App extends Component {
  render() {
    return (
      
      <div className="App">
        <FacebookLogin
          appId="1679927985387347"
          autoLoad={true}
          fields="name,email,picture"
          callback={responseFacebook}
          cssClass="my-facebook-button-class"
          icon="fa-facebook"
        />
      </div>
    );
  }
}


const PROFILE_QUERY = gql`
  query ProfileQuery {
    profile{
      id
      firstName
      lastName
    }
  }
`

// export default graphql(PROFILE_QUERY, { name: 'profile' })(App)

export default App;
