// src/context/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Verifica se l'utente è già autenticato (es. token nel localStorage)
        const token = localStorage.getItem('token');
        if (token) {
            // Decodifica il token e imposta l'utente
            setUser({ token });
        }
    }, []);

    const login = async (credentials) => {
        // Chiamata API per il login
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(credentials),
        });
        const data = await response.json();
        if (data.token) {
            localStorage.setItem('token', data.token);
            setUser({ token: data.token });
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};