package com.example.platform.repository;

import com.example.platform.entity.User;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository {
    User login(User user);
    int register(User user);
}
