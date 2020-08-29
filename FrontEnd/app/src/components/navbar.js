import React from "react";
import Logo from './Curatem Logo.jpg';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <div class='border-b'>
            <div class='flex justify-between mx-10 pb-2'>
                <Link to="/">
                    <img class='-space-x-20' src={Logo} alt='Curatem Logo'></img>
                 </Link>
                 <div class='flex justify-between w-1/4'>
                     <h3 class='self-center'> 
                        <Link to="/categories">
                            Categories
                         </Link>
                      </h3>
                      <input class='self-center h-10 bg-gray-300' type='text' name='name' placeholder='Search' /> 
                    </div>
                 <div class='flex justify-between w-2/12 h-8 self-center'>
                    <h4 class='self-center'>
                        <Link to="/mypaths"> 
                        My Paths 
                        </Link>
                     </h4>
                    <button class='p-1 border border-gray-500 hover:bg-blue-900 hover:text-gray-100'>Log In</button>
                    <button class='p-1 bg-gray-500 text-gray-100 hover:bg-blue-900'>Sign Up</button>
                  </div>
             </div>
         </div>
        )
}

export default Navbar