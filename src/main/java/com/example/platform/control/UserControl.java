package com.example.platform.control;

import com.example.platform.common.result;
import com.example.platform.entity.User;
import com.example.platform.service.UserService;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/user")
public class UserControl {
    @Resource
    private UserService userService;
    @PostMapping("/login")
    public result login(@RequestBody User user) {
        return result.success(userService.login(user));
    }
    @PostMapping("/register")
    public result register(@RequestBody User user) {
        return result.success(userService.register(user));
    }
    @GetMapping("/username/{username}")
    public result finduser(@PathVariable("username") String username) {
        return result.success(userService.selectByUsername(username));
    }
}
