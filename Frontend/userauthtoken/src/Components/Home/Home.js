import React from 'react'
import './Home.css'
import logo from '../../logo.svg';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
const Home = () => {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <h3>
                    Welcome to<br /> Priyanshu Tripathi <br /> Authentication System
                </h3>
                <div className='btn'>
                    <Link to='/login'>  <Button>Login</Button> </Link>
                    <Link> <Button>Registration</Button>   </Link>
                </div>
            </header>
        </div>
    )
}

export default Home
