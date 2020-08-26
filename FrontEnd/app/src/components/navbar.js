import React from "react";
import Logo from './Curatem Logo.jpg';

const Navbar = () => {
    return (
        <div>
            <div class="flex justify-between mx-10">
                 <img class='-space-x-20' src={Logo} alt='Curatem Logo'></img>
                 <div> Categories </div>
                 <input type="text" name="name" placeholder="Search" /> 
                 <div> My Paths </div>
                 <div class="flex justify-between w-1/12">
                    <button>Log In</button>
                    <button>Sign Up</button>
                 </div>
             </div>
         </div>
        )
}

export default Navbar