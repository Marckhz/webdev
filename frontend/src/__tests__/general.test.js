import React from "react";
import {render, screen, cleanup, waitFor } from '@testing-library/react';
import App from "../App";


it("should show App Component", ()=>{
    render(<App/>);
    expect(screen.getByText("Platform Users"));
    expect(screen.getByText("Filter by skill"));
    expect(screen.getByText("Add Users"));
    expect(screen.getByText("Remove Users"));
})

it("should show buttons", () => {
    render(<App/>);
    expect(screen.getByRole('button',{
        name:'Add Users'
    }));
    expect(screen.getByRole('button',{
        name:'Remove Users'
    }));
});

it("should show input", () => {
    render(<App/>);
    expect(screen.getByPlaceholderText('user name'));
});
