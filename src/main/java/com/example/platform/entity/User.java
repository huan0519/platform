package com.example.platform.entity;

import lombok.Data;

@Data
public class User {
    private String username;
    private String password;
    private String avatar_url;
    private String token;
}
