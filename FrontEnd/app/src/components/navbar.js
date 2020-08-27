import React from "react";
import Logo from './Curatem Logo.jpg';

const Navbar = () => {
    return (
        <div>
            <div class="flex justify-between mx-10">
                 <img class='-space-x-20' src={Logo} alt='Curatem Logo'></img>
                 <div class='flex justify-between w-1/4'> 
                     <h3 class="self-center"> Categories
                      </h3>
                      <input type="text" name="name" placeholder="Search" /> 
                    </div>
                 <div class="flex justify-between w-2/12 h-10 self-center">
                    <h4 class="self-center"> My Paths </h4>
                    <button>Log In</button>
                    <button>Sign Up</button>
                  </div>
             </div>
         </div>
        )
}

export default Navbar