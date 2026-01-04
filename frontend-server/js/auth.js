const API_URL = "http://localhost:8000";

export async function login(email, password) {
    const response = await fetch('${API_URL}/auth/login', {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({email, password})
    });
    
    if (!response.ok) {
        throw new Error("Login Fallido");
    }
    
    return response.json();
}