import React from "react";

const Navbar = () => {
    return (
        <div>
            <div class="flex justify-evenly">
                 <h2>Curatem</h2>
                 <div> Search Bar PH</div>
                 <div> Categories </div>
                 <div> My Paths </div>
                 <div class="flex justify-evenly w-1/12">
                    <button>Log In</button>
                    <button>Sign Up</button>
                 </div>
             </div>
         </div>
        )
}

export default Navbar