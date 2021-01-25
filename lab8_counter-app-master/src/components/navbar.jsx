import React from "react";

// Stateless Functional Component

const NavBar = ({ totalCounters }) => {
  return (
    <nav className="navbar navbar-light bg-dark">
      <div className="navbar">
        <i className="fa fa-shopping-basket  " aria-hidden="true" />
        <span className="badge badge-pill badge-info m-2" style={{ width: 100 }}>
          {totalCounters}
        </span>
        Produkty
      </div>
    </nav>
  );
};

export default NavBar;
