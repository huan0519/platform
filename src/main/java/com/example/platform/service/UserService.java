package com.example.platform.service;

import com.example.platform.entity.User;

public interface UserService {
    String login(User user);
    String register(User user);
}
