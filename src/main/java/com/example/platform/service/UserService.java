package com.example.platform.service;

import com.example.platform.common.result;
import com.example.platform.entity.User;

public interface UserService {
    User login(User user);
    User  register(User user);
    User selectByUsername(String username);
}
