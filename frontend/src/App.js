import React, { useState, useEffect } from 'react';
import Home from './pages/Home';
import Signup from './pages/Signup';
import Login from './pages/Login';
import { BrowserRouter as Router } from 'react-router-dom';
import { Routes, Route } from 'react-router-dom';
import { useSelector } from "react-redux"
import { useGetUserQuery } from "./api/core_api"
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { auth } from './firebase';
import { useDispatch } from 'react-redux';
import { setUserData } from './redux/userReducer';

function App() {
  const dispatch = useDispatch();
  const user = useSelector(state => state.user.user);
  // const { data } = useGetUserQuery(
  //   { id: user?.uid }, { skip: !user }
  // )
  // console.log(data, "data")

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      if (user) {
        console.log("UserAutoDetect", user)
        dispatch(setUserData({ user: user }))
      } else {
      }
    });
    return () => unsubscribe();
  }, [])


  return (
    <Router>
      <div>
        <section>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </section>
      </div>
    </Router>
  );
}

export default App;