const API_URL = "http://localhost:8000";

export async function apiGet(endpoint) {
    const response = await fetch('${API_URL}${endpoint}');
    return response.json();
}
